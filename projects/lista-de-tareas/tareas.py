#!/usr/bin/env python3
"""Lista de tareas por línea de comandos. Guarda los datos en tareas.json."""
import argparse
import json
from pathlib import Path

ARCHIVO = Path(__file__).with_name("tareas.json")


def cargar(archivo=ARCHIVO):
    if archivo.exists():
        return json.loads(archivo.read_text(encoding="utf-8"))
    return []


def guardar(tareas, archivo=ARCHIVO):
    archivo.write_text(json.dumps(tareas, ensure_ascii=False, indent=2), encoding="utf-8")


def agregar(tareas, texto):
    tareas.append({"texto": texto, "hecha": False})
    return len(tareas)


def completar(tareas, numero):
    tareas[numero - 1]["hecha"] = True


def eliminar(tareas, numero):
    return tareas.pop(numero - 1)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Lista de tareas")
    sub = parser.add_subparsers(dest="comando", required=True)
    sub.add_parser("listar", help="Mostrar las tareas")
    p = sub.add_parser("agregar", help="Agregar una tarea")
    p.add_argument("texto")
    for nombre in ("completar", "eliminar"):
        p = sub.add_parser(nombre)
        p.add_argument("numero", type=int)
    args = parser.parse_args(argv)

    tareas = cargar()
    try:
        if args.comando == "agregar":
            print(f"Tarea {agregar(tareas, args.texto)} agregada.")
        elif args.comando == "completar":
            completar(tareas, args.numero)
            print(f"Tarea {args.numero} completada.")
        elif args.comando == "eliminar":
            print(f"Eliminada: {eliminar(tareas, args.numero)['texto']}")
        else:
            if not tareas:
                print("No hay tareas.")
            for i, t in enumerate(tareas, 1):
                print(f"{i}. [{'x' if t['hecha'] else ' '}] {t['texto']}")
    except IndexError:
        parser.error(f"No existe la tarea {args.numero}.")
    guardar(tareas)


if __name__ == "__main__":
    main()
