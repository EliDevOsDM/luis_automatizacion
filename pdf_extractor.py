from __future__ import annotations

import re
from dataclasses import dataclass, field
from io import BytesIO
from pathlib import Path

from pypdf import PdfReader
from pypdf.errors import PdfReadError


@dataclass
class DatosAutoAdmite:
    radicado: str = ""
    tipo_proceso: str = ""
    accionante: str = ""
    accionado: str = ""
    vinculados: str = ""
    fecha_auto_admisorio: str = ""
    pretensiones: dict[str, str] = field(default_factory=dict)


_ORDINALES_PRETENSION = (
    "PRIMERA",
    "SEGUNDA",
    "TERCERA",
    "CUARTA",
    "QUINTA",
    "SEXTA",
    "SÉPTIMA",
    "SEPTIMA",
)

_MARCADORES_SIGUIENTE_CAMPO = (
    r"PROCESO\s*:",
    r"ACCIONANTE\s*:",
    r"ACCIONADO\s*:",
    r"ACCIONADA\s*:",
    r"VINCULACI[OÓ]N\s*:",
    r"VINCULADOS\s*:",
    r"RADICACI[OÓ]N\s*:",
    r"RADICADO\s*:",
    r"UBICACI[OÓ]N\s*:",
    r"AUTO\s+ADMITE",
    r"CONSTANCIA",
    r"Bogot[aá]",
    r"RESUELVE",
)

_TAMANO_CABECERA_AUTO = 2500


def _texto_con_pypdf(datos: bytes) -> str:
    reader = PdfReader(BytesIO(datos), strict=False)
    partes: list[str] = []
    for pagina in reader.pages:
        partes.append(pagina.extract_text() or "")
    return "\n".join(partes)


def _texto_con_pymupdf(datos: bytes) -> str:
    import fitz

    documento = fitz.open(stream=datos, filetype="pdf")
    try:
        return "\n".join(pagina.get_text() for pagina in documento)
    finally:
        documento.close()


def _leer_texto_pdf(ruta: Path) -> str:
    datos = ruta.read_bytes()
    if len(datos) < 8 or datos[:4] != b"%PDF":
        raise ValueError(
            f"El archivo no es un PDF válido: {ruta.name} "
            f"({len(datos)} bytes). Vuelva a descargarlo."
        )

    errores: list[str] = []
    for metodo, funcion in (
        ("pymupdf", lambda: _texto_con_pymupdf(datos)),
        ("pypdf", lambda: _texto_con_pypdf(datos)),
    ):
        try:
            texto = funcion()
            if texto.strip():
                return texto
            errores.append(f"{metodo}: sin texto extraíble")
        except (PdfReadError, Exception) as exc:
            errores.append(f"{metodo}: {exc}")

    raise ValueError(
        f"No se pudo leer el PDF {ruta.name}. Intentos: {'; '.join(errores)}"
    )


def _limpiar_valor(texto: str) -> str:
    return re.sub(r"\s+", " ", texto).strip(" .,:;")


def _campo_cabecera_linea(
    texto: str,
    etiquetas: tuple[str, ...],
    *,
    max_chars: int = _TAMANO_CABECERA_AUTO,
) -> str:
    """Campos en las primeras líneas del auto (evita «accionado» en el cuerpo)."""
    cabecera = texto[:max_chars]
    for etiqueta in etiquetas:
        patron = rf"(?im)(?:^|\n)\s*{re.escape(etiqueta)}\s*:?\s*([^\n\r]+)"
        coincidencia = re.search(patron, cabecera)
        if coincidencia:
            valor = _limpiar_valor(coincidencia.group(1))
            if valor:
                return valor
    return ""


def _campo_judicial(texto: str, etiquetas: tuple[str, ...]) -> str:
    fin = "|".join(_MARCADORES_SIGUIENTE_CAMPO)
    for etiqueta in etiquetas:
        patron = (
            rf"{re.escape(etiqueta)}\s*:?\s*"
            rf"(.+?)"
            rf"(?=\n\s*(?:{fin}))"
        )
        coincidencia = re.search(patron, texto, re.IGNORECASE | re.DOTALL)
        if coincidencia:
            valor = _limpiar_valor(coincidencia.group(1))
            if valor:
                return valor
        patron_linea = rf"{re.escape(etiqueta)}\s*:?\s*([^\n]+)"
        coincidencia = re.search(patron_linea, texto, re.IGNORECASE)
        if coincidencia:
            valor = _limpiar_valor(coincidencia.group(1))
            if valor:
                return valor
    return ""


def _extraer_radicado(texto: str) -> str:
    cabecera = texto[:_TAMANO_CABECERA_AUTO]
    coincidencia = re.search(
        r"(?im)(?:RADICACI[OÓ]N|RADICADO)\s*:?\s*(\d{15,25})",
        cabecera,
    )
    if coincidencia:
        return coincidencia.group(1).strip()
    coincidencia = re.search(
        r"(?:RADICACI[OÓ]N|RADICADO)\s*:?\s*([0-9\-]+)",
        cabecera,
        re.IGNORECASE,
    )
    if coincidencia:
        return coincidencia.group(1).strip()
    for etiqueta in ("RADICADO", "RADICACIÓN", "RADICACION"):
        valor = _campo_cabecera_linea(texto, (etiqueta,))
        if valor:
            solo_digitos = re.match(r"(\d{15,25})", valor)
            if solo_digitos:
                return solo_digitos.group(1)
            return valor
    return ""


def _extraer_vinculados(texto: str) -> str:
    coincidencia = re.search(
        r"VINCUL(?:ACI[OÓ]N|ADOS)\s*:?\s*(.+?)(?=\n\s*RADICACI[OÓ]N\s*:)",
        texto,
        re.IGNORECASE | re.DOTALL,
    )
    if coincidencia:
        return _limpiar_valor(coincidencia.group(1))
    return _campo_judicial(texto, ("VINCULADOS", "VINCULACIÓN", "VINCULACION"))


_MARCADORES_FIN_PRETENSIONES_ESCrito = (
    r"(?:^|\n)\s*V\.\s*PRUEBAS",
    r"(?:^|\n)\s*VI\.\s*JURAMENTO",
    r"(?:^|\n)\s*V\.\s*JURAMENTO",
    r"(?:^|\n)\s*VII\.\s*NOTIFICACIONES",
    r"(?:^|\n)\s*III\.\s*DE\s+LOS\s+DERECHOS",
    r"DE\s+LOS\s+DERECHOS\s+DE\s+PETICI",
)

_MARCADORES_INICIO_PRETENSIONES_ESCrito = (
    r"IV\.\s*PRETENSIONES",
    r"PRETENSIÓN\s+DE\s+LA\s+ACCIONANTE",
    r"PRETENSION\s+DE\s+LA\s+ACCIONANTE",
    r"pretendió\s*:",
    r"pretendio\s*:",
    r"(?:^|\n)\s*PRETENSIONES\b",
)

_VERBOS_PRETENSION = (
    r"AMPARAR",
    r"ORDENAR",
    r"DECLARAR",
    r"TUTELAR",
    r"DEJAR\s+SIN\s+EFECTO",
    r"PREVENIR",
    r"CONDENAR",
    r"SOLICITO\s+QUE",
)


def _recortar_bloque_pretensiones_escrito(texto: str) -> str:
    if not texto.strip():
        return ""

    for patron in _MARCADORES_INICIO_PRETENSIONES_ESCrito:
        coincidencia = re.search(patron, texto, re.IGNORECASE)
        if coincidencia:
            fragmento = texto[coincidencia.end() :]
            break
    else:
        primera = re.search(r"\bPRIMERA\.", texto, re.IGNORECASE)
        if not primera:
            return ""
        fragmento = texto[primera.start() :]

    fin = len(fragmento)
    for patron in _MARCADORES_FIN_PRETENSIONES_ESCrito:
        coincidencia = re.search(patron, fragmento, re.IGNORECASE)
        if coincidencia and coincidencia.start() < fin:
            fin = coincidencia.start()

    return fragmento[:fin].strip()


def _extraer_pretensiones_desde_bloque(bloque: str) -> dict[str, str]:
    """Pretensiones PRIMERA… desde el escrito (no PRIMERO del auto)."""
    resultado: dict[str, str] = {}
    if not bloque.strip():
        return resultado

    texto_norm = re.sub(r"\s+", " ", bloque)

    for indice, ordinal in enumerate(_ORDINALES_PRETENSION):
        if ordinal == "SEPTIMA":
            continue
        clave = "SÉPTIMA" if ordinal in ("SÉPTIMA", "SEPTIMA") else ordinal
        if clave in resultado:
            continue

        partes_fin: list[str] = []
        for o in _ORDINALES_PRETENSION[indice + 1 :]:
            if o in ("SÉPTIMA", "SEPTIMA"):
                partes_fin.append(r"(?:\d+\.\s*)?S[ÉE]PTIMA")
            else:
                partes_fin.append(rf"(?:\d+\.\s*)?{re.escape(o)}")
        fin = "|".join(partes_fin)
        fin += (
            r"|(?:\d+\.\s*)?OCTAVA|(?:\d+\.\s*)?NOVENA"
            r"|III\.|V\.\s*JURAMENTO|DE LOS DERECHOS|$"
        )
        token = (
            r"S[ÉE]PTIMA" if ordinal in ("SÉPTIMA", "SEPTIMA") else ordinal
        )
        patron = rf"(?:\d+\.\s*)?{token}\.\s*(.+?)(?=\s*(?:{fin}))"
        coincidencia = re.search(patron, texto_norm, re.IGNORECASE | re.DOTALL)
        if coincidencia:
            valor = _limpiar_valor(coincidencia.group(1))
            if valor and len(valor) > 10:
                resultado[clave] = valor

    return resultado


def _extraer_pretensiones_por_verbos(bloque: str) -> dict[str, str]:
    """Escritos sin PRIMERA/SEGUNDA (p. ej. párrafos AMPARAR… ORDENAR…)."""
    texto = re.sub(r"\s+", " ", bloque).strip()
    intro = re.search(
        r"(?i)(?:señor|senor)\s+juez\s*:?\s*",
        texto,
    )
    if intro:
        texto = texto[intro.end() :].strip()

    alternancia = "|".join(_VERBOS_PRETENSION)
    segmentos = re.findall(
        rf"((?:{alternancia})\b.+?)(?=(?:{alternancia})\b|$)",
        texto,
        flags=re.IGNORECASE | re.DOTALL,
    )
    resultado: dict[str, str] = {}
    for indice, segmento in enumerate(segmentos):
        if indice >= len(_ORDINALES_PRETENSION):
            break
        ordinal = _ORDINALES_PRETENSION[indice]
        if ordinal == "SEPTIMA":
            clave = "SÉPTIMA"
        elif ordinal in ("SÉPTIMA",):
            clave = "SÉPTIMA"
        else:
            clave = ordinal
        valor = _limpiar_valor(segmento)
        if len(valor) > 10:
            resultado[clave] = valor
    return resultado


def extraer_pretensiones_escrito(ruta_pdf: Path) -> dict[str, str]:
    texto = _leer_texto_pdf(ruta_pdf)
    bloque = _recortar_bloque_pretensiones_escrito(texto)
    if not bloque:
        raise ValueError(
            f"No se encontró la sección de pretensiones en {ruta_pdf.name}"
        )
    pretensiones = _extraer_pretensiones_desde_bloque(bloque)
    if not pretensiones:
        pretensiones = _extraer_pretensiones_por_verbos(bloque)
    if not pretensiones:
        raise ValueError(
            f"No se pudieron leer PRIMERA, SEGUNDA… en {ruta_pdf.name}"
        )
    return pretensiones


def _extraer_fecha_auto(texto: str) -> str:
    formato_juzgado = re.search(
        r"\((\d{1,2})\)\s+de\s+([a-záéíóúñA-ZÁÉÍÓÚÑ]+)\s+de\s+[^\(\n]+\((\d{4})\)",
        texto,
        re.IGNORECASE,
    )
    if formato_juzgado:
        return (
            f"{formato_juzgado.group(1)} de {formato_juzgado.group(2).lower()} "
            f"de {formato_juzgado.group(3)}"
        )

    ventana = re.search(
        r"auto admisorio.{0,160}?(\d{1,2}\s+de\s+[a-záéíóúñ]+\s+de\s+\d{4})",
        texto,
        re.IGNORECASE | re.DOTALL,
    )
    if ventana:
        return _limpiar_valor(ventana.group(1))

    coincidencia = re.search(
        r"(\d{1,2}\s+de\s+[a-záéíóúñ]+\s+de\s+\d{4})",
        texto,
        re.IGNORECASE,
    )
    return _limpiar_valor(coincidencia.group(1)) if coincidencia else ""


def extraer_datos_auto_admite(ruta_pdf: Path) -> DatosAutoAdmite:
    texto = _leer_texto_pdf(ruta_pdf)
    if not texto.strip():
        raise ValueError(f"No se pudo leer texto del PDF: {ruta_pdf.name}")

    tipo_proceso = _campo_cabecera_linea(
        texto, ("TIPO DE PROCESO", "PROCESO", "REFERENCIA")
    )
    if not tipo_proceso:
        tipo_proceso = _campo_judicial(texto, ("TIPO DE PROCESO", "PROCESO"))

    datos = DatosAutoAdmite(
        radicado=_extraer_radicado(texto),
        tipo_proceso=tipo_proceso,
        accionante=_campo_cabecera_linea(texto, ("ACCIONANTE",)),
        accionado=_campo_cabecera_linea(
            texto, ("ACCIONADO", "ACCIONADA")
        ),
        vinculados=_extraer_vinculados(texto),
        fecha_auto_admisorio=_extraer_fecha_auto(texto),
        pretensiones={},
    )

    faltantes = [
        nombre
        for nombre, valor in [
            ("radicado", datos.radicado),
            ("accionante", datos.accionante),
        ]
        if not valor
    ]
    if faltantes:
        raise ValueError(
            f"PDF incompleto; no se extrajeron: {', '.join(faltantes)}"
        )

    return datos
