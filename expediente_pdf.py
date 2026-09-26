from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass


@dataclass
class AnexoExpediente:
    titulo: str
    url: str
    puntaje: int


def _normalizar(texto: str) -> str:
    sin_acentos = unicodedata.normalize("NFKD", texto)
    sin_acentos = sin_acentos.encode("ascii", "ignore").decode("ascii")
    return sin_acentos.lower()


def _puntaje_anexo_auto_admite(titulo: str) -> int:
    """Mayor puntaje = mejor candidato para auto que admite y vincula."""
    norm = _normalizar(titulo)
    if not norm.strip():
        return -1

    puntaje = 0
    tiene_admite = "admite" in norm or "admision" in norm or "admisorio" in norm
    tiene_vincula = "vincula" in norm

    if tiene_admite and tiene_vincula:
        puntaje += 100
    elif tiene_admite:
        puntaje += 40
    elif "auto" in norm and tiene_vincula:
        puntaje += 30
    else:
        return -1

    if norm.endswith(".pdf") or ".pdf" in norm:
        puntaje += 5
    if "auto" in norm:
        puntaje += 10
    if re.search(r"\d{2}auto", norm.replace(" ", "")):
        puntaje += 5

    return puntaje


def _puntaje_anexo_escrito(titulo: str) -> int:
    """Escrito de tutela con pretensiones (p. ej. 01EscritoyAnexos.pdf)."""
    norm = _normalizar(titulo)
    if not norm.strip():
        return -1

    compacto = re.sub(r"[\s_\-]+", "", norm)
    if "admite" in norm or "vincula" in norm:
        return -1
    if "auto" in norm and ("adm" in norm or "admite" in compacto):
        return -1

    puntaje = 0
    if "escritoyanexos" in compacto or "escritoyanexo" in compacto:
        puntaje += 100
    if "escrito" in norm and "anexo" in norm:
        puntaje += 85
    elif "escrito" in norm:
        puntaje += 35

    if re.search(r"\b01", norm) or compacto.startswith("01"):
        puntaje += 10
    if norm.endswith(".pdf") or ".pdf" in norm:
        puntaje += 5

    return puntaje if puntaje > 0 else -1


def elegir_anexo_escrito(candidatos: list[dict]) -> AnexoExpediente | None:
    mejores: list[AnexoExpediente] = []
    for item in candidatos:
        titulo = (item.get("titulo") or item.get("texto") or "").strip()
        url = (item.get("url") or "").strip()
        if not url:
            continue
        puntaje = _puntaje_anexo_escrito(titulo)
        if puntaje < 0:
            continue
        mejores.append(AnexoExpediente(titulo=titulo, url=url, puntaje=puntaje))

    if not mejores:
        return None

    mejores.sort(key=lambda a: (-a.puntaje, len(a.titulo)))
    return mejores[0]


def elegir_anexo_auto_admite(candidatos: list[dict]) -> AnexoExpediente | None:
    mejores: list[AnexoExpediente] = []
    for item in candidatos:
        titulo = (item.get("titulo") or item.get("texto") or "").strip()
        url = (item.get("url") or "").strip()
        if not url:
            continue
        puntaje = _puntaje_anexo_auto_admite(titulo)
        if puntaje < 0:
            continue
        mejores.append(AnexoExpediente(titulo=titulo, url=url, puntaje=puntaje))

    if not mejores:
        return None

    mejores.sort(key=lambda a: (-a.puntaje, len(a.titulo)))
    return mejores[0]


def nombre_archivo_descarga(titulo: str) -> str:
    limpio = re.sub(r"[<>:\"/\\|?*]", "_", titulo)
    limpio = re.sub(r"\s+", "_", limpio).strip("._")
    if not limpio:
        limpio = "auto_admite_vincula"
    if not limpio.lower().endswith(".pdf"):
        limpio += ".pdf"
    return limpio[:180]
