from __future__ import annotations

import re
import time
from dataclasses import dataclass
from typing import Callable

from playwright.sync_api import Page, TimeoutError as PlaywrightTimeoutError

LogFn = Callable[[str], None]


@dataclass
class DestinatarioGestion:
    """Destinatario externo (contacto del juzgado), no el firmante del MEN."""

    nombre: str
    entidad: str


def leer_destinatario_gestion(page: Page) -> DestinatarioGestion:
    nombre = _texto_selector(page, "#contacto")
    entidad = _texto_selector(page, "#cliente")
    if not nombre and not entidad:
        entidad = _texto_selector(page, "#infoNegocio label:has-text('Despacho') + span")
    return DestinatarioGestion(nombre=nombre, entidad=entidad)


def crear_comunicacion_externa(
    page: Page,
    log: LogFn,
    destinatario: DestinatarioGestion,
) -> None:
    log("  → Iniciando comunicación externa en SGDEA…")
    _cerrar_modales_bloqueantes(page)

    boton_menu = page.locator("#accionCrearDocs #dropdownCrearDocumento")
    boton_menu.wait_for(state="visible", timeout=30_000)
    boton_menu.scroll_into_view_if_needed()
    boton_menu.click()

    opcion = page.locator(
        'a.dropdown-item[data-nombre="Comunicación externa"], '
        'a.dropdown-item:has-text("Comunicación externa")'
    ).first
    opcion.wait_for(state="visible", timeout=15_000)
    opcion.click()

    _esperar_creacion_documento(page, log)
    _responder_modal_ultimo_documento(page, log)
    _esperar_editor_documento(page, log)

    if destinatario.nombre or destinatario.entidad:
        _abrir_y_llenar_destinatario_externo(page, log, destinatario)
    else:
        log(
            "  → No se leyó contacto/entidad en la gestión; "
            "complete destinatario manualmente."
        )


def _texto_selector(page: Page, selector: str) -> str:
    loc = page.locator(selector).first
    try:
        if not loc.is_visible(timeout=2_000):
            return ""
        return (loc.inner_text() or "").strip()
    except PlaywrightTimeoutError:
        return ""


def _cerrar_modales_bloqueantes(page: Page) -> None:
    for selector in (
        "#gestionarDetalle #modalExpediente.show button.close",
        "#modalExpediente.show button.close",
        ".modal.show button.close",
    ):
        boton = page.locator(selector).first
        try:
            if boton.is_visible(timeout=1_500):
                boton.click()
                time.sleep(0.4)
        except PlaywrightTimeoutError:
            continue


def _esperar_creacion_documento(page: Page, log: LogFn) -> None:
    alerta = page.locator(".sweet-alert")
    try:
        alerta.wait_for(state="visible", timeout=12_000)
        log("  → SGDEA creando comunicación externa (espere)…")
        page.wait_for_function(
            """() => {
                const el = document.querySelector('.sweet-alert');
                if (!el) return true;
                const style = window.getComputedStyle(el);
                if (style.display === 'none') return true;
                return el.classList.contains('hideSweetAlert');
            }""",
            timeout=180_000,
        )
    except PlaywrightTimeoutError:
        pass


def _responder_modal_ultimo_documento(page: Page, log: LogFn) -> None:
    modal = page.locator("#modalUltimoDoc")
    try:
        visible = page.wait_for_function(
            """() => {
                const m = document.querySelector('#modalUltimoDoc');
                if (!m) return false;
                return m.classList.contains('show')
                    || window.getComputedStyle(m).display !== 'none';
            }""",
            timeout=8_000,
        )
        if not visible:
            return
    except PlaywrightTimeoutError:
        return

    log("  → Modal «¿Este documento finaliza la gestión?» → Sí")
    page.locator("#txUltimoDocSi").check(force=True)
    page.locator("#guardarUltimoDoc").click()
    try:
        modal.wait_for(state="hidden", timeout=30_000)
    except PlaywrightTimeoutError:
        page.locator("#modalUltimoDoc .close").click()


def _esperar_editor_documento(page: Page, log: LogFn) -> None:
    page.wait_for_selector("#frameVerDocumentos", state="visible", timeout=120_000)
    page.wait_for_function(
        """() => {
            const frame = document.querySelector('#frameVerDocumentos');
            if (!frame || !frame.src) return false;
            return frame.src.includes('EditorDocumentalRich');
        }""",
        timeout=120_000,
    )
    log("  → Editor de comunicación externa cargado.")
    time.sleep(1.5)


def _frame_editor(page: Page):
    return page.frame_locator("#frameVerDocumentos")


def _abrir_y_llenar_destinatario_externo(
    page: Page,
    log: LogFn,
    destinatario: DestinatarioGestion,
) -> None:
    log(
        f"  → Destinatario (contacto juzgado): {destinatario.nombre or '?'} | "
        f"Entidad: {destinatario.entidad or '?'}"
    )
    frame = _frame_editor(page)
    enlace = frame.locator("#DestinatarioExterno").first
    enlace.wait_for(state="visible", timeout=60_000)
    enlace.click()

    _esperar_dialogo_destinatario(page)
    if _intentar_asignar_destinatario_existente(page, log, destinatario):
        log("  → Destinatario asignado desde búsqueda.")
        return

    if _intentar_nuevo_destinatario(page, log, destinatario):
        log("  → Formulario de destinatario externo completado.")
        return

    log(
        "  → No se pudo automatizar el formulario de destinatario; "
        "revise el modal «Destinatario Externo»."
    )


def _esperar_dialogo_destinatario(page: Page) -> None:
    for selector in (
        "#TMSDialogModalDialogFind.show",
        "#TMSDialogModalDialogFind[style*='display: block']",
        "#TMSDialogModalDialog.show",
        "#TMSDialogModalDialog[style*='display: block']",
    ):
        try:
            page.locator(selector).wait_for(state="visible", timeout=25_000)
            return
        except PlaywrightTimeoutError:
            continue
    time.sleep(2)


def _raiz_dialogo(page: Page):
    for selector in (
        "#TMSDialogModalContentDialogFind",
        "#TMSDialogModalContentDialog",
    ):
        loc = page.locator(selector)
        if loc.count() and loc.first.is_visible():
            return loc.first
    return page.locator("body")


def _intentar_asignar_destinatario_existente(
    page: Page,
    log: LogFn,
    destinatario: DestinatarioGestion,
) -> bool:
    if not destinatario.nombre:
        return False

    raiz = _raiz_dialogo(page)
    buscador = raiz.locator(
        "input[type='search'], input[placeholder*='uscar' i], "
        "input[placeholder*='destinatario' i]"
    ).first
    try:
        if not buscador.is_visible(timeout=5_000):
            return False
        buscador.fill("")
        buscador.fill(destinatario.nombre)
        time.sleep(1.2)
    except PlaywrightTimeoutError:
        return False

    fila = raiz.locator("table tbody tr").filter(
        has_text=re.compile(re.escape(destinatario.nombre[:20]), re.I)
    ).first
    try:
        if fila.is_visible(timeout=5_000):
            fila.click()
            _clic_boton_guardar_dialogo(page)
            return True
    except PlaywrightTimeoutError:
        pass

    return False


def _intentar_nuevo_destinatario(
    page: Page,
    log: LogFn,
    destinatario: DestinatarioGestion,
) -> bool:
    raiz = _raiz_dialogo(page)
    nuevo = raiz.locator(
        "button:has-text('Nuevo destinatario'), a:has-text('Nuevo destinatario')"
    ).first
    try:
        if nuevo.is_visible(timeout=4_000):
            nuevo.click()
            time.sleep(0.8)
    except PlaywrightTimeoutError:
        pass

    asignado = page.evaluate(
        """({ nombre, entidad }) => {
            const roots = [
                document.querySelector('#TMSDialogModalContentDialogFind'),
                document.querySelector('#TMSDialogModalContentDialog'),
                document.body,
            ].filter(Boolean);

            const setByLabel = (root, fragment, value) => {
                if (!value) return false;
                const labels = [...root.querySelectorAll('label')];
                const lab = labels.find((l) =>
                    (l.innerText || '').toLowerCase().includes(fragment)
                );
                if (!lab) return false;
                let input = null;
                const id = lab.getAttribute('for');
                if (id) input = root.querySelector('#' + CSS.escape(id));
                if (!input) {
                    const block = lab.closest('.form-group, .form-row, .col-12, div');
                    if (block) {
                        input = block.querySelector(
                            'input:not([type=hidden]), textarea, select'
                        );
                    }
                }
                if (!input) return false;
                if (input.tagName === 'SELECT') {
                    const opts = [...input.options];
                    const hit = opts.find((o) =>
                        (o.text || '').toLowerCase().includes(value.toLowerCase())
                    );
                    if (hit) {
                        input.value = hit.value;
                        input.dispatchEvent(new Event('change', { bubbles: true }));
                        return true;
                    }
                    return false;
                }
                input.focus();
                input.value = value;
                input.dispatchEvent(new Event('input', { bubbles: true }));
                input.dispatchEvent(new Event('change', { bubbles: true }));
                return true;
            };

            let ok = false;
            for (const root of roots) {
                if (setByLabel(root, 'tipo destinatario', 'jurídica')) ok = true;
                if (setByLabel(root, 'título', 'señor')) ok = true;
                if (setByLabel(root, 'prefijo', 'señor')) ok = true;
                if (setByLabel(root, 'destinatario', nombre)) ok = true;
                if (setByLabel(root, 'nombre entidad', entidad)) ok = true;
            }
            return ok;
        }""",
        {"nombre": destinatario.nombre, "entidad": destinatario.entidad},
    )

    if not asignado:
        return False

    _clic_boton_guardar_dialogo(page)
    return True


def _clic_boton_guardar_dialogo(page: Page) -> None:
    for selector in (
        "#TMSDialogHtmlModalOk",
        "#TMSDialogHtmlModalOkWoV",
        "button.btn-primary:has-text('Guardar')",
        "button:has-text('Asignar')",
    ):
        boton = page.locator(selector).first
        try:
            if boton.is_visible(timeout=3_000):
                boton.click()
                time.sleep(0.8)
                return
        except PlaywrightTimeoutError:
            continue
