"""
EX04 (Texto) · Listín telefónico en fichero

Vas a implementar un pequeño "CRUD" (Crear/Leer/Actualizar/Borrar) de contactos,
guardados en un fichero de texto.

Formato del fichero (una línea por contacto):
nombre,telefono

Ejemplo:
Ana,600123123
Luis,600000000

Para que el ejercicio sea más limpio, se proponen dos funciones "privadas":
- _load_phonebook(): lee el fichero y lo convierte en dict
- _save_phonebook(): guarda el dict en el fichero

Luego, las funciones públicas usan esas helpers:
- add_contact(): alta/actualización
- get_phone(): consulta
- remove_contact(): baja
"""

from __future__ import annotations

from pathlib import Path


def _load_phonebook(path: str | Path) -> dict[str, str]:
    path = Path(path)

    # Si no existe, no es error
    if not path.exists():
        return {}

    phonebook: dict[str, str] = {}

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()

            # Ignorar líneas vacías
            if not line:
                continue

            parts = line.split(",")

            if len(parts) != 2:
                raise ValueError("Línea mal formada en el listín")

            name, phone = parts[0].strip(), parts[1].strip()
            phonebook[name] = phone

    return phonebook


def _save_phonebook(path: str | Path, phonebook: dict[str, str]) -> None:
    path = Path(path)

    with path.open("w", encoding="utf-8") as f:
        for name, phone in phonebook.items():
            f.write(f"{name},{phone}\n")


def add_contact(path: str | Path, name: str, phone: str) -> None:
    name = name.strip()
    phone = phone.strip()

    if not name or not phone:
        raise ValueError("Nombre y teléfono no pueden estar vacíos")

    phonebook = _load_phonebook(path)
    phonebook[name] = phone
    _save_phonebook(path, phonebook)


def get_phone(path: str | Path, name: str) -> str | None:
    name = name.strip()

    if not Path(path).exists():
        return None

    phonebook = _load_phonebook(path)
    return phonebook.get(name)


def remove_contact(path: str | Path, name: str) -> bool:
    name = name.strip()
    path = Path(path)

    if not path.exists():
        return False

    phonebook = _load_phonebook(path)

    if name not in phonebook:
        return False

    del phonebook[name]
    _save_phonebook(path, phonebook)
    return True
