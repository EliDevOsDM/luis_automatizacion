from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


LOGIN_URL = (
    "https://sgdea.mineducacion.gov.co/TMS.Solution.MENGESDOC/"
    "(SwgUB8M7)/CR/es/Home/Corporativo"
)


@dataclass
class Credenciales:
    usuario: str
    contrasena: str


@dataclass
class FilaCorreo:
    asunto: str
    firmante: str
    cargo: str
    revisores_ciclo_adhoc: str
    cargo_revisor: str


@dataclass
class ConfigApp:
    credenciales: Credenciales
    radicados: list[str]
    correos: list[FilaCorreo]


def _cell_str(value) -> str:
    if value is None or (isinstance(value, float) and pd.isna(value)):
        return ""
    return str(value).strip()


def _normalize_password_column(df: pd.DataFrame) -> pd.DataFrame:
    for col in df.columns:
        if col.strip().lower().startswith("contrase"):
            df = df.rename(columns={col: "Contraseña"})
            break
    return df


def cargar_config(ruta: Path) -> ConfigApp:
    if not ruta.is_file():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    hojas = pd.read_excel(ruta, sheet_name=None)

    if "Credenciales" not in hojas:
        raise ValueError('Falta la hoja "Credenciales" en config.xlsx')
    if "Radicados a depurar" not in hojas:
        raise ValueError('Falta la hoja "Radicados a depurar" en config.xlsx')

    cred_df = _normalize_password_column(hojas["Credenciales"].copy())
    if cred_df.empty:
        raise ValueError("La hoja Credenciales está vacía")
    if "Usuario" not in cred_df.columns or "Contraseña" not in cred_df.columns:
        raise ValueError('Credenciales debe tener columnas "Usuario" y "Contraseña"')

    fila = cred_df.iloc[0]
    credenciales = Credenciales(
        usuario=_cell_str(fila["Usuario"]),
        contrasena=_cell_str(fila["Contraseña"]),
    )
    if not credenciales.usuario or not credenciales.contrasena:
        raise ValueError("Usuario o contraseña vacíos en Credenciales")

    rad_df = hojas["Radicados a depurar"]
    col_radicado = None
    for col in rad_df.columns:
        if "radicado" in str(col).lower():
            col_radicado = col
            break
    if col_radicado is None:
        raise ValueError('No se encontró columna de radicado en "Radicados a depurar"')

    radicados: list[str] = []
    for value in rad_df[col_radicado]:
        texto = _cell_str(value)
        if texto:
            radicados.append(texto)

    correos: list[FilaCorreo] = []
    if "Correos" in hojas:
        corr_df = hojas["Correos"]
        for _, row in corr_df.iterrows():
            correos.append(
                FilaCorreo(
                    asunto=_cell_str(row.get("Asunto", "")),
                    firmante=_cell_str(row.get("Firmante", "")),
                    cargo=_cell_str(row.get("Cargo", "")),
                    revisores_ciclo_adhoc=_cell_str(row.get("Revisores ciclo adHoc", "")),
                    cargo_revisor=_cell_str(row.get("Cargo Revisor", "")),
                )
            )

    return ConfigApp(
        credenciales=credenciales,
        radicados=radicados,
        correos=correos,
    )
