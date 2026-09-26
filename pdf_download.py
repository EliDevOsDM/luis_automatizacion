from __future__ import annotations

import base64
import re
from typing import Callable
from urllib.parse import urljoin

from playwright.sync_api import BrowserContext, Page, Response

LogFn = Callable[[str], None]

BASE_SGDEA = "https://sgdea.mineducacion.gov.co"
_PATRON_UUID = re.compile(
    r"GestorArchivo/(?:Ver|Obtener|Renderizar)/([0-9a-f-]{36})",
    re.IGNORECASE,
)


def _es_pdf(contenido: bytes) -> bool:
    return len(contenido) > 4 and contenido[:4] == b"%PDF"


def _describir_inicio(contenido: bytes) -> str:
    muestra = contenido[:160]
    if muestra.startswith(b"<!") or b"<html" in muestra.lower():
        return "HTML (visor o página de error)"
    return muestra.decode("utf-8", errors="replace").replace("\n", " ")[:120]


def _url_absoluta(url: str, referer: str) -> str:
    if url.startswith("http://") or url.startswith("https://"):
        return url
    if url.startswith("/"):
        return BASE_SGDEA + url
    return urljoin(referer.rstrip("/") + "/", url)


def _prefijo_gestor_archivo(url_absoluta: str) -> str | None:
    coincidencia = _PATRON_UUID.search(url_absoluta)
    if not coincidencia:
        return None
    inicio = url_absoluta.lower().find("gestorarchivo")
    if inicio < 0:
        return None
    return url_absoluta[: inicio + len("GestorArchivo")]


def _urls_descarga_desde_enlace(url: str, referer: str) -> list[str]:
    """Ver/Renderizar son visor HTML; Obtener entrega el PDF."""
    absoluta = _url_absoluta(url, referer)
    prefijo = _prefijo_gestor_archivo(absoluta)
    coincidencia = _PATRON_UUID.search(absoluta)
    if not prefijo or not coincidencia:
        return []

    uuid = coincidencia.group(1)
    return [
        f"{prefijo}/Obtener/{uuid}",
        f"{prefijo}/Renderizar/{uuid}",
    ]


def _clic_tarjeta_expediente(page: Page, url_tarjeta: str) -> None:
    page.evaluate(
        """(targetUrl) => {
            const cards = document.querySelectorAll(
                '#expedienteDetalle .card[data-url]'
            );
            for (const card of cards) {
                if (card.getAttribute('data-url') === targetUrl) {
                    card.scrollIntoView({ block: 'center' });
                    card.click();
                    return true;
                }
            }
            return false;
        }""",
        url_tarjeta,
    )


def _selector_modal_expediente() -> str:
    return "#gestionarDetalle #modalExpediente"


def _urls_en_modal(page: Page) -> list[str]:
    return page.evaluate(
        """() => {
            const modal =
                document.querySelector('#gestionarDetalle #modalExpediente') ||
                document.querySelector('#modalExpediente.show') ||
                document.querySelector('#modalExpediente');
            if (!modal) return [];
            const urls = [];
            modal.querySelectorAll('a[href]').forEach((a) => {
                const href = a.getAttribute('href') || '';
                if (href.includes('GestorArchivo/Obtener')) urls.push(href);
            });
            modal.querySelectorAll('iframe, embed, object').forEach((el) => {
                const src = el.getAttribute('src') || el.getAttribute('data');
                if (src) urls.push(src);
            });
            const html = modal.innerHTML || '';
            const patrones = [
                /\\/GestorArchivo\\/Obtener\\/[0-9a-f-]+/gi,
                /\\/GestorArchivo\\/Renderizar\\/[0-9a-f-]+/gi,
                /\\/GestorArchivo\\/Ver\\/[0-9a-f-]+/gi,
            ];
            for (const re of patrones) {
                let m;
                while ((m = re.exec(html)) !== null) urls.push(m[0]);
            }
            return [...new Set(urls)];
        }"""
    )


def _fetch_en_pagina(page: Page, url: str) -> bytes:
    b64 = page.evaluate(
        """async (targetUrl) => {
            const response = await fetch(targetUrl, { credentials: 'include' });
            if (!response.ok) {
                throw new Error('HTTP ' + response.status);
            }
            const buffer = await response.arrayBuffer();
            const bytes = new Uint8Array(buffer);
            let binary = '';
            const chunkSize = 0x8000;
            for (let i = 0; i < bytes.length; i += chunkSize) {
                const slice = bytes.subarray(i, i + chunkSize);
                binary += String.fromCharCode.apply(null, slice);
            }
            return btoa(binary);
        }""",
        url,
    )
    return base64.b64decode(b64)


def _intentar_urls_descarga(
    page: Page,
    context: BrowserContext,
    urls: list[str],
    referer: str,
    log: LogFn | None,
) -> tuple[bytes, str] | None:
    cabeceras = {
        "Referer": referer,
        "Accept": "application/pdf,application/octet-stream,*/*",
    }
    vistos: set[str] = set()

    for enlace in urls:
        absoluta = _url_absoluta(enlace, referer)
        for candidata in _urls_descarga_desde_enlace(absoluta, referer) or [absoluta]:
            if candidata in vistos:
                continue
            vistos.add(candidata)

            if log:
                log(f"  → Descargando: …{candidata[-55:]}")

            for nombre, obtener in (
                ("fetch", lambda u=candidata: _fetch_en_pagina(page, u)),
                (
                    "API",
                    lambda u=candidata: context.request.get(
                        u, headers=cabeceras, timeout=120_000
                    ).body(),
                ),
            ):
                try:
                    cuerpo = obtener()
                    if _es_pdf(cuerpo):
                        if log:
                            log(
                                f"  → PDF válido ({len(cuerpo) // 1024} KB) vía {nombre}."
                            )
                        return cuerpo, candidata
                except Exception as exc:
                    if log:
                        log(f"  → {nombre} falló: {exc}")

    return None


def _respuesta_parece_pdf(respuesta: Response) -> bool:
    if not respuesta.ok:
        return False
    url = respuesta.url.lower()
    if "/gestorarchivo/obtener/" in url or "/gestorarchivo/renderizar/" in url:
        return True
    tipo = (respuesta.headers.get("content-type") or "").lower()
    return "pdf" in tipo or "octet-stream" in tipo


def _intentar_guardar_respuesta(respuesta: Response, destino: dict) -> None:
    if not _respuesta_parece_pdf(respuesta):
        return
    try:
        cuerpo = respuesta.body()
    except Exception:
        return
    if not _es_pdf(cuerpo):
        return
    if not destino.get("bytes") or len(cuerpo) > len(destino["bytes"]):
        destino["bytes"] = cuerpo
        destino["url"] = respuesta.url


def descargar_pdf_abriendo_visor(
    page: Page,
    context: BrowserContext,
    url_tarjeta: str,
    log: LogFn | None = None,
) -> bytes:
    referer = page.url
    urls_prioritarias = _urls_descarga_desde_enlace(url_tarjeta, referer)

    if urls_prioritarias:
        if log:
            log("  → Intentando GestorArchivo/Obtener (PDF real)…")
        resultado = _intentar_urls_descarga(
            page, context, urls_prioritarias, referer, log
        )
        if resultado:
            cuerpo, _ = resultado
            if log:
                log("  → Abriendo visor en pantalla…")
            _clic_tarjeta_expediente(page, url_tarjeta)
            page.locator(_selector_modal_expediente()).first.wait_for(
                state="visible", timeout=45_000
            )
            return cuerpo

    captura: dict = {}

    def _listener(respuesta: Response) -> None:
        _intentar_guardar_respuesta(respuesta, captura)

    page.on("response", _listener)
    try:
        if log:
            log("  → Abriendo PDF en visor del expediente…")
        _clic_tarjeta_expediente(page, url_tarjeta)

        modal = page.locator(_selector_modal_expediente()).first
        modal.wait_for(state="visible", timeout=45_000)

        page.wait_for_function(
            """() => {
                const modal = document.querySelector(
                    '#gestionarDetalle #modalExpediente'
                );
                if (!modal) return false;
                return !!(
                    modal.querySelector('iframe[src*="GestorArchivo"]') ||
                    modal.querySelector('a[href*="GestorArchivo/Obtener"]') ||
                    modal.innerHTML.includes('GestorArchivo')
                );
            }""",
            timeout=45_000,
        )

        for _ in range(15):
            if captura.get("bytes"):
                break
            page.wait_for_timeout(400)

        urls_modal = _urls_en_modal(page)
        todas = urls_prioritarias + urls_modal + [url_tarjeta]
        if not captura.get("bytes"):
            resultado = _intentar_urls_descarga(
                page, context, todas, referer, log
            )
            if resultado:
                return resultado[0]

        if captura.get("bytes"):
            if log:
                log(
                    f"  → PDF capturado en red "
                    f"({len(captura['bytes']) // 1024} KB)."
                )
            return captura["bytes"]

        raise RuntimeError(
            "No se obtuvo el PDF. El enlace Ver/Renderizar es solo visor HTML; "
            "falló GestorArchivo/Obtener."
        )
    finally:
        page.remove_listener("response", _listener)


def descargar_pdf_autenticado(
    page: Page,
    context: BrowserContext,
    url: str,
    log: LogFn | None = None,
) -> bytes:
    referer = page.url
    urls = _urls_descarga_desde_enlace(url, referer)
    if not urls:
        urls = [_url_absoluta(url, referer)]

    resultado = _intentar_urls_descarga(page, context, urls, referer, log)
    if resultado:
        return resultado[0]

    raise RuntimeError(
        f"No se pudo descargar PDF desde {url}. "
        f"Último intento no devolvió bytes %PDF."
    )
