from src.dominio.datos_pokedex import DATOS_POKEMON, EVOLUCIONES
from src.dominio.pokemon import Pokemon


class Pokedex:
    """Administra el catálogo y sus cadenas de evoluciones."""

    def __init__(self, pokemons, evoluciones):
        self.pokemons = pokemons
        self.evoluciones = evoluciones

    @classmethod
    def crear_inicial(cls):
        """Crea la Pokédex con los datos provistos para el trabajo."""
        pokemons = []

        for datos in DATOS_POKEMON:
            pokemon = Pokemon(
                datos["id"],
                datos["nombre"],
                datos["tipo1"],
                datos["tipo2"],
                datos["hp"],
                datos["ataque"],
                datos["defensa"],
                datos["velocidad"],
                datos["generacion"],
            )
            pokemons.append(pokemon)

        return cls(pokemons, EVOLUCIONES)

    def listar(self):
        """Muestra todos los Pokémon del catálogo."""
        print("\n--- CATÁLOGO POKÉDEX ---")

        for pokemon in self.pokemons:
            print(pokemon)

        print(f"\nTotal de Pokémon: {len(self.pokemons)}")

    def buscar_por_id(self, pokemon_id):
        """Busca un Pokémon por número. Devuelve None si no existe."""
        for pokemon in self.pokemons:
            if pokemon.id == pokemon_id:
                return pokemon
        return None

    def obtener_cadenas_evolutivas(self, pokemon_id):
        """Devuelve todos los caminos evolutivos desde un Pokémon."""
        if self.buscar_por_id(pokemon_id) is None:
            return []
        return self._construir_cadenas(pokemon_id)

    def _construir_cadenas(self, pokemon_id):
        """Construye recursivamente los caminos de evolución."""
        pokemon = self.buscar_por_id(pokemon_id)
        siguientes = self.evoluciones.get(pokemon_id, [])

        # Caso base: si no tiene evoluciones, la cadena termina aquí.
        if not siguientes:
            return [[pokemon]]

        cadenas = []

        # Caso recursivo: se obtienen las cadenas de cada evolución y se
        # agrega el Pokémon actual al comienzo de cada una.
        for siguiente_id in siguientes:
            cadenas_siguientes = self._construir_cadenas(siguiente_id)

            for cadena in cadenas_siguientes:
                cadenas.append([pokemon] + cadena)

        return cadenas

    def mostrar_cadenas_evolutivas(self, pokemon_id):
        """Muestra en pantalla las cadenas evolutivas solicitadas."""
        cadenas = self.obtener_cadenas_evolutivas(pokemon_id)

        if not cadenas:
            print(f"No existe un Pokémon con el número {pokemon_id}.")
            return

        print("\n--- CADENA EVOLUTIVA ---")

        for cadena in cadenas:
            nombres = []
            for pokemon in cadena:
                nombres.append(pokemon.nombre)
            print(" -> ".join(nombres))
