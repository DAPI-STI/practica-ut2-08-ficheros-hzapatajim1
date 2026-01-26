"""
EX03 (CSV) · Calcular la media de una columna

Objetivo:
- Leer un CSV con cabecera (primera línea).
- Usar la librería estándar `csv` (recomendado: csv.DictReader).
- Convertir datos a float y calcular una media.

Ejemplo típico:
- Un CSV de calificaciones con columnas: name, average
"""

from __future__ import annotations

from pathlib import Path
import csv


def csv_average(path: str | Path, column: str) -> float:
    """
    Calcula y devuelve la media de la columna numérica `column` en el CSV `path`.
    """

    path = Path(path)

    total = 0.0
    count = 0

    # Abrir el fichero (lanza FileNotFoundError si no existe)
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)

        # Comprobar que la columna existe
        if reader.fieldnames is None or column not in reader.fieldnames:
            raise ValueError(f"La columna '{column}' no existe en el CSV")

        for row in reader:
            try:
                value = float(row[column])
            except (ValueError, TypeError):
                raise ValueError(f"Valor no numérico en la columna '{column}'")

            total += value
            count += 1

    # No hay filas de datos
    if count == 0:
        raise ValueError("El CSV no contiene filas de datos")

    return total / count