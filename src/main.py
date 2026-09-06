from src.config import TEMA
from src.persistencia.texto import cargar_csv


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


def crear_pokemon(fila):
    """Convierte una fila del CSV en un Pokémon."""
    return {
        "id": int(fila["id"]),
        "nombre": fila["nombre"],
        "tipo1": fila["tipo1"],
        "tipo2": fila["tipo2"],
        "hp": int(fila["hp"]),
        "ataque": int(fila["ataque"]),
        "defensa": int(fila["defensa"]),
        "velocidad": int(fila["velocidad"]),
        "generacion": int(fila["generacion"]),
    }


def cargar_catalogo():
    """Carga los Pokémon del archivo CSV."""
    filas = cargar_csv("data/pokedex.csv")
    catalogo = []

    for fila in filas:
        pokemon = crear_pokemon(fila)
        catalogo.append(pokemon)

    return catalogo


def listar_catalogo(catalogo):
    """Muestra todos los Pokémon cargados."""
    print("\n--- CATÁLOGO POKÉDEX ---")

    for pokemon in catalogo:
        tipos = pokemon["tipo1"]

        if pokemon["tipo2"]:
            tipos = tipos + " / " + pokemon["tipo2"]

        print(
            f'#{pokemon["id"]:03d} | '
            f'{pokemon["nombre"]} | '
            f'Tipo: {tipos} | '
            f'HP: {pokemon["hp"]} | '
            f'Ataque: {pokemon["ataque"]} | '
            f'Defensa: {pokemon["defensa"]} | '
            f'Velocidad: {pokemon["velocidad"]} | '
            f'Generación: {pokemon["generacion"]}'
        )

    print(f"\nTotal de Pokémon: {len(catalogo)}")


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    try:
        catalogo = cargar_catalogo()
    except (FileNotFoundError, ValueError) as error:
        print(f"Error al cargar el catálogo: {error}")
        return

    opcion = None

    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            listar_catalogo(catalogo)
        elif opcion in {"2", "3", "4", "5", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
