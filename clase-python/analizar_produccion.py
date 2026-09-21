"""Analiza el CSV del caso. Uso: python analizar_produccion.py [archivo.csv]."""
import sys
from pathlib import Path
import numpy as np
import pandas as pd

def validar_datos(tabla):
    requeridas = ["fecha", "linea", "producidas", "defectuosas", "horas", "operarios", "meta"]
    faltantes = set(requeridas) - set(tabla.columns)
    if faltantes:
        raise ValueError(f"Faltan columnas: {sorted(faltantes)}")
    if tabla.empty:
        raise ValueError("No hay registros")
    datos = tabla[requeridas].copy()
    datos["fecha"] = pd.to_datetime(datos["fecha"], errors="coerce")
    datos["linea"] = datos["linea"].astype("string").str.strip().str.upper()
    numericas = ["producidas", "defectuosas", "horas", "operarios", "meta"]
    for columna in numericas:
        datos[columna] = pd.to_numeric(datos[columna], errors="coerce")
    if datos.isna().any().any():
        raise ValueError("Hay ausentes, fechas inválidas o números no convertibles")
    if not np.isfinite(datos[numericas].to_numpy(dtype=float)).all():
        raise ValueError("Hay números infinitos")
    if not datos["linea"].isin(["A", "B"]).all():
        raise ValueError("Línea fuera del catálogo A/B")
    if datos.duplicated(["fecha", "linea"]).any():
        raise ValueError("Clave fecha-línea duplicada")
    enteras = ["producidas", "defectuosas", "operarios", "meta"]
    if ((datos[enteras] % 1) != 0).any().any():
        raise ValueError("Los conteos deben ser enteros")
    if (datos[["producidas", "defectuosas"]] < 0).any().any():
        raise ValueError("Conteos negativos")
    if (datos["defectuosas"] > datos["producidas"]).any():
        raise ValueError("Defectuosas supera producidas")
    if (datos[["horas", "operarios", "meta"]] <= 0).any().any():
        raise ValueError("Horas, operarios y meta deben ser positivos")
    return datos

def agregar_indicadores(datos):
    tabla = datos.copy()
    tabla["buenas"] = tabla["producidas"] - tabla["defectuosas"]
    tabla["horas_persona"] = tabla["horas"] * tabla["operarios"]
    denominador = tabla["producidas"].replace(0, np.nan)
    tabla["calidad_pct"] = tabla["buenas"] / denominador * 100
    tabla["rechazo_pct"] = tabla["defectuosas"] / denominador * 100
    tabla["cumplimiento_pct"] = tabla["producidas"] / tabla["meta"] * 100
    tabla["producidas_hora"] = tabla["producidas"] / tabla["horas"]
    tabla["buenas_hora"] = tabla["buenas"] / tabla["horas"]
    tabla["productividad_laboral"] = tabla["buenas"] / tabla["horas_persona"]
    tabla["estado_calidad"] = np.select(
        [tabla["calidad_pct"].isna(), tabla["calidad_pct"] >= 98, tabla["calidad_pct"] >= 95],
        ["Sin producción", "Verde", "Amarillo"], default="Rojo")
    return tabla

def resumir(tabla, grupos):
    columnas = ["producidas", "defectuosas", "buenas", "horas", "horas_persona", "meta"]
    resumen = tabla.groupby(grupos, as_index=False)[columnas].sum()
    resumen["calidad_pct"] = resumen["buenas"] / resumen["producidas"].replace(0, np.nan) * 100
    resumen["cumplimiento_pct"] = resumen["producidas"] / resumen["meta"] * 100
    resumen["productividad_laboral"] = resumen["buenas"] / resumen["horas_persona"]
    return resumen

def main():
    origen = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).with_name("produccion.csv")
    tabla = agregar_indicadores(validar_datos(pd.read_csv(origen)))
    resumen = resumir(tabla, "linea")
    destino = Path("resultados")
    destino.mkdir(exist_ok=True)
    tabla.to_csv(destino / "detalle_indicadores.csv", index=False, encoding="utf-8-sig")
    resumen.to_csv(destino / "resumen_por_linea.csv", index=False, encoding="utf-8-sig")
    print(resumen.round(2).to_string(index=False))
    print("Resultados en", destino.resolve())

if __name__ == "__main__":
    main()
