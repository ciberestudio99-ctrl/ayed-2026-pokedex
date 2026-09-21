from src.config import TEMA
from src.dominio.pokedex import Pokedex


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}


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


def pedir_numero_pokemon():
    """Solicita un número de Pokédex y valida que sea entero."""
    texto = input("Número de Pokémon: ").strip()

    try:
        return int(texto)
    except ValueError:
        print("El número debe ser un entero.")
        return None


def ver_detalle(pokedex):
    """Muestra el detalle de un Pokémon elegido por número."""
    pokemon_id = pedir_numero_pokemon()

    if pokemon_id is None:
        return

    pokemon = pokedex.buscar_por_id(pokemon_id)

    if pokemon is None:
        print(f"No existe un Pokémon con el número {pokemon_id}.")
    else:
        print("\n--- DETALLE DEL POKÉMON ---")
        print(pokemon)


def ver_cadena_evolutiva(pokedex):
    """Solicita un Pokémon y ejecuta la operación recursiva."""
    pokemon_id = pedir_numero_pokemon()

    if pokemon_id is not None:
        pokedex.mostrar_cadenas_evolutivas(pokemon_id)


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    pokedex = Pokedex.crear_inicial()
    opcion = None

    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()

        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            pokedex.listar()
        elif opcion == "2":
            ver_detalle(pokedex)
        elif opcion == "5":
            ver_cadena_evolutiva(pokedex)
        elif opcion in {"3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
