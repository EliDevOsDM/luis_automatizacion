from __future__ import annotations

import threading
import tkinter as tk
from pathlib import Path
from tkinter import filedialog, messagebox, scrolledtext, ttk

from config_loader import cargar_config
from sgdea_automation import AutomatizacionSGDEA

BASE_DIR = Path(__file__).resolve().parent
CONFIG_DEFAULT = BASE_DIR / "config.xlsx"


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Automatización SGDEA — MEN")
        self.geometry("720x520")
        self.minsize(640, 420)

        self.config_path = tk.StringVar(value=str(CONFIG_DEFAULT))
        self.headless = tk.BooleanVar(value=False)
        self._worker: threading.Thread | None = None
        self._bot: AutomatizacionSGDEA | None = None
        self._config = None

        self._build_ui()
        self._cargar_vista_config()

    def _build_ui(self) -> None:
        marco = ttk.Frame(self, padding=12)
        marco.pack(fill=tk.BOTH, expand=True)

        fila_cfg = ttk.Frame(marco)
        fila_cfg.pack(fill=tk.X, pady=(0, 8))
        ttk.Label(fila_cfg, text="config.xlsx:").pack(side=tk.LEFT)
        ttk.Entry(fila_cfg, textvariable=self.config_path).pack(
            side=tk.LEFT, fill=tk.X, expand=True, padx=6
        )
        ttk.Button(fila_cfg, text="Examinar…", command=self._elegir_config).pack(side=tk.LEFT)
        ttk.Button(fila_cfg, text="Recargar", command=self._cargar_vista_config).pack(
            side=tk.LEFT, padx=(6, 0)
        )

        self.lbl_resumen = ttk.Label(marco, text="", wraplength=660)
        self.lbl_resumen.pack(fill=tk.X, pady=(0, 8))

        opciones = ttk.Frame(marco)
        opciones.pack(fill=tk.X, pady=(0, 8))
        ttk.Checkbutton(
            opciones,
            text="Ejecutar navegador en segundo plano (headless)",
            variable=self.headless,
        ).pack(side=tk.LEFT)

        botones = ttk.Frame(marco)
        botones.pack(fill=tk.X, pady=(0, 8))
        self.btn_iniciar = ttk.Button(botones, text="Iniciar automatización", command=self._iniciar)
        self.btn_iniciar.pack(side=tk.LEFT)
        self.btn_detener = ttk.Button(
            botones, text="Detener", command=self._detener, state=tk.DISABLED
        )
        self.btn_detener.pack(side=tk.LEFT, padx=(8, 0))

        ttk.Label(marco, text="Registro:").pack(anchor=tk.W)
        self.log = scrolledtext.ScrolledText(marco, height=18, state=tk.DISABLED, wrap=tk.WORD)
        self.log.pack(fill=tk.BOTH, expand=True, pady=(4, 0))

    def _elegir_config(self) -> None:
        ruta = filedialog.askopenfilename(
            title="Seleccionar config.xlsx",
            filetypes=[("Excel", "*.xlsx"), ("Todos", "*.*")],
            initialdir=str(BASE_DIR),
        )
        if ruta:
            self.config_path.set(ruta)
            self._cargar_vista_config()

    def _escribir_log(self, mensaje: str) -> None:
        def _append() -> None:
            self.log.configure(state=tk.NORMAL)
            self.log.insert(tk.END, mensaje + "\n")
            self.log.see(tk.END)
            self.log.configure(state=tk.DISABLED)

        self.after(0, _append)

    def _cargar_vista_config(self) -> None:
        try:
            self._config = cargar_config(Path(self.config_path.get()))
        except Exception as exc:
            self._config = None
            self.lbl_resumen.configure(
                text=f"No se pudo leer la configuración: {exc}",
                foreground="red",
            )
            return

        n_rad = len(self._config.radicados)
        n_corr = len(self._config.correos)
        usuario = self._config.credenciales.usuario
        self.lbl_resumen.configure(
            text=(
                f"Usuario: {usuario} | Radicados a depurar: {n_rad} | "
                f"Filas en Correos (próxima fase): {n_corr}"
            ),
            foreground="",
        )
        self._escribir_log("Configuración recargada.")

    def _iniciar(self) -> None:
        if self._worker and self._worker.is_alive():
            messagebox.showinfo("En ejecución", "Ya hay una automatización en curso.")
            return

        try:
            config = cargar_config(Path(self.config_path.get()))
        except Exception as exc:
            messagebox.showerror("Configuración", str(exc))
            return

        if not config.radicados:
            if not messagebox.askyesno(
                "Sin radicados",
                "No hay radicados en el Excel. ¿Continuar solo con inicio de sesión y navegación?",
            ):
                return

        self.btn_iniciar.configure(state=tk.DISABLED)
        self.btn_detener.configure(state=tk.NORMAL)

        self._bot = AutomatizacionSGDEA(
            config,
            self._escribir_log,
            headless=self.headless.get(),
        )

        def _run() -> None:
            try:
                self._bot.ejecutar()
            except Exception:
                pass
            finally:
                self.after(0, self._finalizar_worker)

        self._worker = threading.Thread(target=_run, daemon=True)
        self._worker.start()
        self._escribir_log("--- Inicio de automatización ---")

    def _detener(self) -> None:
        if self._bot:
            self._bot.solicitar_detener()
            self._escribir_log("Solicitud de detención enviada…")

    def _finalizar_worker(self) -> None:
        self.btn_iniciar.configure(state=tk.NORMAL)
        self.btn_detener.configure(state=tk.DISABLED)
        self._escribir_log("--- Fin del proceso ---")


def main() -> None:
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
