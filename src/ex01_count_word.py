"""
EX01 (Texto) · Buscar una palabra en un fichero

Objetivo:
- Practicar la lectura de ficheros de texto usando `open(...)`.
- Normalizar el contenido (minúsculas) y contar coincidencias.

Consejo:
- No hace falta una solución "perfecta" de NLP.
  Con que cuentes palabras separadas por espacios y elimines puntuación básica es suficiente.
"""

from __future__ import annotations

from pathlib import Path
import string


def count_word_in_file(path: str | Path, word: str) -> int:
    """
    Devuelve el número de apariciones de `word` dentro del fichero de texto `path`.
    """

    # Validar la palabra
    if not word or word.strip() == "":
        raise ValueError("La palabra no puede estar vacía o contener solo espacios")

    path = Path(path)

    # Abrir fichero (esto lanzará FileNotFoundError si no existe)
    with path.open("r", encoding="utf-8") as f:
        text = f.read()

    # Normalizar a minúsculas
    text = text.lower()
    word = word.lower().strip()

    # Reemplazar la puntuación por espacios
    translator = str.maketrans(string.punctuation, " " * len(string.punctuation))
    text = text.translate(translator)

    # Separar en palabras
    words = text.split()

    # Contar coincidencias exactas
    return words.count(word)