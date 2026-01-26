"""
EX02 (CSV) · Registrar calificaciones finales

Objetivo:
- Practicar escritura en ficheros en modo "append" (añadir al final).
- Guardar datos en un formato estándar: CSV (separado por comas).

En una app real esto sería el típico "registro" de resultados.
"""

from __future__ import annotations

from pathlib import Path

def write_final_grade(path: str | Path, name: str, average: float) -> None:
    """
    Añade una línea al fichero CSV en `path` con formato:
    nombre,nota
    """

    # Validar nombre
    if not name or name.strip() == "":
        raise ValueError("El nombre no puede estar vacío")

    # Validar nota
    if not (0 <= average <= 10):
        raise ValueError("La nota debe estar entre 0 y 10")

    path = Path(path)

    # Abrir en modo append (crear si no existe)
    with path.open("a", encoding="utf-8") as f:
        f.write(f"{name.strip()},{average}\n")