class Pokemon:
    """Representa un Pokémon del catálogo."""

    def __init__(
        self,
        id,
        nombre,
        tipo1,
        tipo2,
        hp,
        ataque,
        defensa,
        velocidad,
        generacion,
    ):
        self.id = id
        self.nombre = nombre
        self.tipo1 = tipo1
        self.tipo2 = tipo2
        self.hp = hp
        self.ataque = ataque
        self.defensa = defensa
        self.velocidad = velocidad
        self.generacion = generacion

    def obtener_tipos(self):
        """Devuelve los tipos listos para mostrarlos en pantalla."""
        if self.tipo2:
            return self.tipo1 + " / " + self.tipo2
        return self.tipo1

    def descripcion(self):
        """Devuelve todos los datos del Pokémon en una sola línea."""
        return (
            f"#{self.id:03d} | {self.nombre} | "
            f"Tipo: {self.obtener_tipos()} | "
            f"HP: {self.hp} | Ataque: {self.ataque} | "
            f"Defensa: {self.defensa} | Velocidad: {self.velocidad} | "
            f"Generación: {self.generacion}"
        )

    def __str__(self):
        return self.descripcion()
