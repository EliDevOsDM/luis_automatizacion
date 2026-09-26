from __future__ import annotations

import time
from pathlib import Path
from typing import Callable

from playwright.sync_api import (
    BrowserContext,
    Page,
    TimeoutError as PlaywrightTimeoutError,
    sync_playwright,
)

from config_loader import LOGIN_URL, ConfigApp
from expediente_pdf import (
    AnexoExpediente,
    elegir_anexo_auto_admite,
    elegir_anexo_escrito,
    nombre_archivo_descarga,
)
from pdf_download import descargar_pdf_abriendo_visor, descargar_pdf_autenticado
from pdf_extractor import extraer_datos_auto_admite, extraer_pretensiones_escrito
from plantilla_word import PLANTILLA_DEFAULT, llenar_plantilla

BASE_DIR = Path(__file__).resolve().parent

LogFn = Callable[[str], None]

_ORDEN_PRETENSION_LOG = (
    "PRIMERA",
    "SEGUNDA",
    "TERCERA",
    "CUARTA",
    "QUINTA",
    "SEXTA",
    "SÉPTIMA",
)


def _orden_pretension(clave: str) -> int:
    try:
        return _ORDEN_PRETENSION_LOG.index(clave)
    except ValueError:
        return 99


class AutomatizacionSGDEA:
    def __init__(
        self,
        config: ConfigApp,
        log: LogFn,
        *,
        headless: bool = False,
        pausa_entre_radicados_s: float = 1.5,
    ) -> None:
        self.config = config
        self.log = log
        self.headless = headless
        self.pausa_entre_radicados_s = pausa_entre_radicados_s
        self._detener = False

    def solicitar_detener(self) -> None:
        self._detener = True

    def ejecutar(self) -> None:
        self._detener = False
        with sync_playwright() as pw:
            browser = pw.chromium.launch(headless=self.headless)
            context = browser.new_context(locale="es-CO")
            page = context.new_page()
            page.set_default_timeout(60_000)

            try:
                self._iniciar_sesion(page)
                self._ir_a_gestionar(page)
                self._buscar_radicados(page, context)
                self.log("Automatización completada (fase actual).")
            except Exception as exc:
                self.log(f"Error: {exc}")
                raise
            finally:
                if not self.headless:
                    self.log(
                        "Navegador abierto 10 minutos para revisión "
                        "(o ciérralo manualmente)."
                    )
                    for _ in range(600):
                        if self._detener:
                            break
                        time.sleep(1)
                browser.close()

    def _iniciar_sesion(self, page: Page) -> None:
        self.log("Abriendo página de inicio de sesión…")
        page.goto(LOGIN_URL, wait_until="domcontentloaded")

        page.locator("#UserId").fill(self.config.credenciales.usuario)
        page.locator("#PassWord").fill(self.config.credenciales.contrasena)
        self.log("Credenciales cargadas desde config.xlsx.")
        page.locator("#aceptar").click()

        page.wait_for_load_state("networkidle")
        self.log("Sesión iniciada.")

    def _ir_a_gestionar(self, page: Page) -> None:
        self.log("Esperando tablero de mis asignadas…")
        page.wait_for_selector("#barSecuenciaAbiertas1", state="visible", timeout=90_000)

        canvas = page.locator("#barSecuenciaAbiertas1")
        self.log("Abriendo detalle de comunicaciones (gráfico de secuencias)…")
        canvas.click(force=True)

        buscador_selector = "#tblGestionar_filter input[type='search']"
        try:
            page.wait_for_selector(buscador_selector, state="visible", timeout=25_000)
        except PlaywrightTimeoutError:
            self.log("Reintentando vía enlace 'Comunicaciones' del tablero…")
            page.locator("a.ma-gestionar-t").first.click()
            page.wait_for_selector(buscador_selector, state="visible", timeout=90_000)

        self.log("Tabla de gestión lista.")

    def _buscar_radicados(self, page: Page, context: BrowserContext) -> None:
        buscador = page.locator("#tblGestionar_filter input[type='search']")
        total = len(self.config.radicados)
        if total == 0:
            self.log("No hay radicados en la hoja 'Radicados a depurar'.")
            return

        self.log(f"Buscando {total} radicado(s) en tblGestionar…")
        for indice, radicado in enumerate(self.config.radicados, start=1):
            if self._detener:
                self.log("Detenido por el usuario.")
                break

            self.log(f"[{indice}/{total}] Buscando: {radicado}")
            self._filtrar_tabla_radicado(page, buscador, radicado)

            try:
                self._esperar_boton_gestion(page, radicado)
                visibles = page.locator(
                    "#tblGestionar tbody tr:has(button.gestion)"
                ).filter(has_text=radicado)
                self.log(
                    f"  → Filas filtradas con botón gestionar: {visibles.count()}"
                )
                self._clic_boton_gestion(page, radicado)
                self._descargar_pdf_y_llenar_plantilla(page, context, radicado)
            except PlaywrightTimeoutError:
                self.log("  → No apareció el botón gestionar tras filtrar.")
            except RuntimeError as exc:
                self.log(f"  → {exc}")
            except Exception as exc:
                self.log(f"  → Error procesando documentos: {exc}")

            if indice < total:
                self._volver_a_lista_gestionar(page)

            time.sleep(self.pausa_entre_radicados_s)

    def _filtrar_tabla_radicado(self, page: Page, buscador, radicado: str) -> None:
        page.locator("#gestionarTabla").scroll_into_view_if_needed()
        page.evaluate(
            """(rad) => {
                const input = document.querySelector(
                    "#tblGestionar_filter input[type='search']"
                );
                if (window.jQuery && window.jQuery.fn.dataTable) {
                    const $t = window.jQuery("#tblGestionar");
                    if (window.jQuery.fn.dataTable.isDataTable($t)) {
                        $t.DataTable().search(rad).draw();
                        return;
                    }
                }
                if (input) {
                    input.focus();
                    input.value = rad;
                    input.dispatchEvent(new Event("input", { bubbles: true }));
                    input.dispatchEvent(new Event("keyup", { bubbles: true }));
                }
            }""",
            radicado,
        )
        buscador.click()
        buscador.fill(radicado)
        self._esperar_datatable_listo(page)
        page.wait_for_function(
            """(rad) => {
                const info = document.querySelector("#tblGestionar_info");
                const txt = info ? info.innerText : "";
                if (txt.includes("0 de un total de 0")) return false;
                if (txt.includes("1 de un total de 1")) return true;
                let n = 0;
                document.querySelectorAll("#tblGestionar tbody tr").forEach((row) => {
                    if (row.classList.contains("child")) return;
                    if (row.innerText.includes(rad) && row.querySelector("button.gestion")) {
                        n += 1;
                    }
                });
                return n === 1;
            }""",
            arg=radicado,
            timeout=60_000,
        )

    def _esperar_datatable_listo(self, page: Page) -> None:
        page.wait_for_function(
            """() => {
                const proc = document.querySelector("#tblGestionar_processing");
                if (proc && proc.style.display !== "none") return false;
                return true;
            }""",
            timeout=60_000,
        )

    def _esperar_boton_gestion(self, page: Page, radicado: str) -> None:
        page.wait_for_function(
            """(rad) => {
                const proc = document.querySelector("#tblGestionar_processing");
                if (proc && proc.style.display !== "none") return false;
                const info = document.querySelector("#tblGestionar_info");
                const infoTxt = info ? info.innerText : "";
                const rows = document.querySelectorAll("#tblGestionar tbody tr");
                let filaRad = 0;
                for (const row of rows) {
                    if (row.classList.contains("child")) continue;
                    if (!row.innerText.includes(rad)) continue;
                    if (row.querySelector("button.gestion")) filaRad += 1;
                }
                if (filaRad === 1) return true;
                if (infoTxt.includes("0 de un total de 0")) return false;
                return filaRad >= 1 && infoTxt.includes("1 de un total de 1");
            }""",
            arg=radicado,
            timeout=60_000,
        )

    def _clic_boton_gestion(self, page: Page, radicado: str) -> None:
        self.log("  → Clic en botón Gestionar (engranaje)…")
        clicado = page.evaluate(
            """(rad) => {
                const rows = document.querySelectorAll("#tblGestionar tbody tr");
                for (const row of rows) {
                    if (row.classList.contains("child")) continue;
                    if (!row.innerText.includes(rad)) continue;
                    const btn = row.querySelector("button.gestion");
                    if (!btn) continue;
                    btn.scrollIntoView({ block: "center", inline: "center" });
                    btn.click();
                    return true;
                }
                return false;
            }""",
            radicado,
        )
        if not clicado:
            raise RuntimeError(
                f"No se encontró el botón gestionar para el radicado {radicado}."
            )

        try:
            page.wait_for_function(
                """() => {
                    const cont = document.querySelector("#containerGestionar");
                    const det = document.querySelector("#gestionarDetalle");
                    if (!cont || !det) return false;
                    const visible = !cont.classList.contains("oculto");
                    const hasContent = (det.innerHTML || "").trim().length > 0;
                    return visible || hasContent;
                }""",
                timeout=60_000,
            )
            self.log("  → Detalle de gestión abierto.")
        except PlaywrightTimeoutError:
            page.wait_for_load_state("networkidle")
            self.log("  → Clic enviado; verifique la pantalla de gestión.")

    def _volver_a_lista_gestionar(self, page: Page) -> None:
        buscador = "#tblGestionar_filter input[type='search']"
        if page.locator(buscador).is_visible():
            return

        self.log("  → Volviendo a la lista de radicados…")
        clicado = False
        for selector in ("#verTableroAPP", "a.ma-gestionar-t", "#recargarDetalleAPP"):
            enlace = page.locator(selector).first
            try:
                if enlace.is_visible(timeout=2_000):
                    enlace.click()
                    clicado = True
                    break
            except PlaywrightTimeoutError:
                continue
        if not clicado:
            page.go_back()
            page.wait_for_load_state("domcontentloaded")

        page.wait_for_selector(buscador, state="visible", timeout=90_000)

    @staticmethod
    def _listar_anexos_expediente(page: Page) -> list[dict]:
        return page.evaluate(
            """() => {
                const cards = document.querySelectorAll(
                    '#expedienteDetalle .card[data-url]'
                );
                return Array.from(cards).map((card) => {
                    const detalle = card.querySelector('.expediente-detalle');
                    const titulo = detalle
                        ? detalle.innerText.split('\\n').filter(Boolean)[0] || ''
                        : card.innerText.split('\\n').filter(Boolean)[0] || '';
                    return {
                        titulo: titulo.trim(),
                        url: card.getAttribute('data-url') || '',
                    };
                });
            }"""
        )

    def _descargar_anexo_a_carpeta(
        self,
        page: Page,
        context: BrowserContext,
        anexo: AnexoExpediente,
        carpeta: Path,
        *,
        abrir_visor: bool,
    ) -> Path:
        ruta = carpeta / nombre_archivo_descarga(anexo.titulo)
        if abrir_visor:
            try:
                contenido = descargar_pdf_abriendo_visor(
                    page, context, anexo.url, log=self.log
                )
            except RuntimeError:
                self.log("  → Reintentando descarga directa por URL…")
                contenido = descargar_pdf_autenticado(
                    page, context, anexo.url, log=self.log
                )
        else:
            contenido = descargar_pdf_autenticado(
                page, context, anexo.url, log=self.log
            )

        ruta.write_bytes(contenido)
        self.log(f"  → PDF guardado: {ruta.name}")
        return ruta

    def _descargar_pdf_y_llenar_plantilla(
        self,
        page: Page,
        context: BrowserContext,
        radicado_sgdea: str,
    ) -> None:
        self.log(
            "  → Buscando auto admisorio y escrito con anexos en el expediente…"
        )
        page.wait_for_selector("#expedienteDetalle", state="visible", timeout=60_000)
        page.locator("#collapseExpediente").scroll_into_view_if_needed()
        time.sleep(0.5)

        candidatos = self._listar_anexos_expediente(page)
        anexo = elegir_anexo_auto_admite(candidatos)
        if not anexo:
            nombres = ", ".join(
                (c.get("titulo") or "?")[:40] for c in candidatos[:8]
            )
            raise RuntimeError(
                "No se encontró un PDF del auto admisorio (admite + vincula). "
                f"Anexos visibles: {nombres or 'ninguno'}"
            )

        anexo_escrito = elegir_anexo_escrito(candidatos)
        if not anexo_escrito:
            nombres = ", ".join(
                (c.get("titulo") or "?")[:40] for c in candidatos[:12]
            )
            raise RuntimeError(
                "No se encontró el escrito con anexos (01EscritoyAnexos.pdf). "
                f"Anexos visibles: {nombres or 'ninguno'}"
            )

        carpeta = BASE_DIR / "salida" / radicado_sgdea
        carpeta.mkdir(parents=True, exist_ok=True)

        self.log(f"  → Anexo auto: {anexo.titulo}")
        ruta_pdf = self._descargar_anexo_a_carpeta(
            page, context, anexo, carpeta, abrir_visor=True
        )

        self.log(f"  → Escrito anexo: {anexo_escrito.titulo}")
        ruta_escrito = self._descargar_anexo_a_carpeta(
            page, context, anexo_escrito, carpeta, abrir_visor=False
        )

        self.log("  → Extrayendo datos del auto admisorio…")
        datos = extraer_datos_auto_admite(ruta_pdf)
        self.log(
            f"  → Radicado judicial: {datos.radicado} | Accionante: {datos.accionante}"
        )

        self.log("  → Extrayendo pretensiones del escrito (hasta juramento)…")
        datos.pretensiones = extraer_pretensiones_escrito(ruta_escrito)
        self.log(
            "  → Pretensiones: "
            + ", ".join(sorted(datos.pretensiones.keys(), key=_orden_pretension))
        )

        ruta_docx = carpeta / f"Plantilla_{radicado_sgdea}.docx"
        llenar_plantilla(datos, ruta_docx, plantilla=PLANTILLA_DEFAULT)
        self.log(f"  → Word generado: {ruta_docx}")

        self.log(
            "  → El PDF queda abierto en el modal del expediente "
            "(ciérrelo con la X cuando termine de revisar)."
        )
