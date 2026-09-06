# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Integrante: Rodrigo Nahuel Aquino
- Tema: Pokédex

Elegí el tema Pokédex porque me pareció claro y fácil de relacionar con un catálogo.
Cada Pokémon se puede representar mediante diferentes datos, como su número, nombre y tipo.
Esto permite practicar la lectura y organización de información desde un archivo CSV.
También me resulta sencillo entender que la Pokédex contiene una colección de Pokémon.
Durante las próximas entregas se podrán agregar búsquedas, ordenamientos y evoluciones.
Elegí este tema porque creo que me ayudará a comprender mejor las estructuras de datos.

## 2. Modelo

Un ítem del catálogo representa un Pokémon. Cada Pokémon tiene los campos id, nombre, tipo1, tipo2, hp, ataque, defensa, velocidad y generación.

En la Entrega 1, cada Pokémon se representará mediante un diccionario. El catálogo será una lista que contendrá todos los diccionarios cargados desde `data/pokedex.csv`.

La lista del catálogo y los diccionarios son mutables porque permiten agregar, eliminar o modificar elementos. Los números enteros y las cadenas de texto son inmutables: cuando cambia uno de esos valores, Python lo reemplaza por otro.

En entregas posteriores, la colección principal será el equipo de Pokémon. El historial se implementará mediante una pila y los turnos de combate mediante una cola.

Lista inicial del modelo:

- Pokémon: un ítem cargado desde el CSV.
- Catálogo: colección de todos los Pokémon.
- Equipo: colección principal, con un máximo de seis Pokémon.
- Historial: pila de acciones.
- Turnos de combate: cola de Pokémon.

## 3. Recursión (E2)

- Función:
- Caso base:
- Caso recursivo:
- Traza de un ejemplo real del dataset:

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
