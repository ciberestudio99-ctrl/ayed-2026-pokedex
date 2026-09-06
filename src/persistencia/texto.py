import csv


def cargar_csv(ruta):
    """Carga un archivo CSV y devuelve una lista de diccionarios."""
    with open(ruta, "r", encoding="utf-8", newline="") as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)


def guardar_csv(ruta, filas, encabezados):
    raise NotImplementedError