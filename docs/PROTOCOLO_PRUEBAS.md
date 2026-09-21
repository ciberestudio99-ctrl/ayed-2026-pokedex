# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Iniciar; elegir `1`; luego `0` | opción 1 | lista 70 Pokémon y vuelve al menú sin traceback | pasa | Regresión de E1 verificada el 20/09/2026 |
| P02 | E2 | Iniciar; elegir `2`; ingresar `25`; luego `0` | Pikachu | muestra el detalle completo de Pikachu y vuelve al menú | pasa | Verificado el 20/09/2026 |
| P03 | E2 | Iniciar; elegir `2`; ingresar `-1`; luego `0` | id inexistente | muestra “No existe” y el menú sigue funcionando | pasa | Verificado el 20/09/2026 |
| P04 | E2 | Iniciar; elegir `5`; ingresar `1`; luego `0` | Bulbasaur | imprime `Bulbasaur -> Ivysaur -> Venusaur` | pasa | Cadena lineal verificada el 20/09/2026 |
| P05 | E2 | Iniciar; elegir `5`; ingresar `3`; luego `0` | Venusaur | imprime solamente `Venusaur` | pasa | Caso base verificado el 20/09/2026 |
| P06 | E2 | Iniciar; elegir `5`; ingresar `133`; luego `0` | Eevee | imprime tres cadenas: Vaporeon, Jolteon y Flareon | pasa | Ramificación verificada el 20/09/2026 |
| P07 | E2 | Iniciar; elegir `5`; ingresar `172`; luego `0` | Pichu | imprime `Pichu -> Pikachu -> Raichu` | pasa | Cadena entre generaciones verificada el 20/09/2026 |
| P08 | E2 | Iniciar; elegir `5`; ingresar `abc`; luego `0` | texto no numérico | muestra “El número debe ser un entero” y el menú continúa | pasa | Validación verificada el 20/09/2026 |
| P09 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia |  |  |
| P10 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue |  |  |
| P11 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue |  |  |
| P12 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones |  |  |
| P13 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P14 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P15 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P16 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P17 | E5 | Guardar texto (`.txt`), salir, volver a entrar |  | los datos siguen |  |  |
| P18 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P19 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
