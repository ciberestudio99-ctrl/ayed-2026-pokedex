# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Integrante: Rodrigo Nahuel Aquino
- Tema: Pokédex

Elegí el tema Pokédex porque me pareció claro y fácil de relacionar con un catálogo.
Cada Pokémon se puede representar mediante diferentes datos, como su número, nombre y tipo.
Esto permite practicar la organización de información dentro de un catálogo.
También me resulta sencillo entender que la Pokédex contiene una colección de Pokémon.
Durante las próximas entregas se podrán agregar búsquedas, ordenamientos y evoluciones.
Elegí este tema porque creo que me ayudará a comprender mejor las estructuras de datos.

## 2. Modelo

Un ítem del catálogo representa un Pokémon. Cada Pokémon tiene los campos id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad y generación.

En la Entrega 2, cada Pokémon es un objeto de la clase `Pokemon`, ubicada en `src/dominio/pokemon.py`. La clase `Pokedex`, ubicada en `src/dominio/pokedex.py`, administra la lista de objetos, el listado, la búsqueda por número y las cadenas evolutivas. Los datos iniciales y las relaciones de evolución están en `src/dominio/datos_pokedex.py`. Los archivos de `data/` se empezarán a leer recién en la Entrega 5.

La lista del catálogo y los objetos son mutables porque permiten agregar, eliminar o modificar elementos. Los números enteros y las cadenas de texto son inmutables: cuando cambia uno de esos valores, Python lo reemplaza por otro.

En entregas posteriores, la colección principal será el equipo de Pokémon. El historial se implementará mediante una pila y los turnos de combate mediante una cola.

Lista inicial del modelo:

- Pokémon: objeto que representa un ítem del catálogo.
- Pokédex: objeto que administra la lista de Pokémon y sus evoluciones.
- Catálogo: lista que contiene objetos `Pokemon`.
- Equipo: colección principal, con un máximo de seis Pokémon.
- Historial: pila de acciones.
- Turnos de combate: cola de Pokémon.

## 3. Recursión (E2)

- Función: `Pokedex._construir_cadenas(pokemon_id)`.
- Caso base: si el Pokémon no tiene evoluciones siguientes, devuelve una lista que contiene una única cadena con ese Pokémon: `[[pokemon]]`.
- Caso recursivo: para cada evolución siguiente, la función se llama a sí misma. Después agrega el Pokémon actual al comienzo de cada cadena obtenida.
- Resultado: devuelve una lista de caminos. Esto permite representar también las tres evoluciones posibles de Eevee.

### Traza: Bulbasaur (número 1)

1. `_construir_cadenas(1)` encuentra a Bulbasaur y su siguiente evolución, el número 2.
2. Llama a `_construir_cadenas(2)`, que encuentra a Ivysaur y llama al número 3.
3. `_construir_cadenas(3)` encuentra a Venusaur. Como no tiene una evolución siguiente, se cumple el caso base y devuelve `[[Venusaur]]`.
4. La llamada del número 2 antepone a Ivysaur y devuelve `[[Ivysaur, Venusaur]]`.
5. La llamada del número 1 antepone a Bulbasaur y devuelve `[[Bulbasaur, Ivysaur, Venusaur]]`.

La salida mostrada en el menú es:

```text
Bulbasaur -> Ivysaur -> Venusaur
```

## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
|  |  |  |  |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
|  |  |  |

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
