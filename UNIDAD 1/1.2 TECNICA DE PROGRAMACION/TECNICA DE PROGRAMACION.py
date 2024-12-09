class Personaje:
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def mostrar_atributos(self):
        print(f"{self.nombre}:")
        print(f"  Fuerza: {self.fuerza}")
        print(f"  Inteligencia: {self.inteligencia}")
        print(f"  Defensa: {self.defensa}")
        print(f"  Vida: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, cantidad):
        self.vida -= cantidad
        if self.vida <= 0:
            self.vida = 0
            print(f"{self.nombre} ha muerto.")

    def calcular_daño(self, enemigo):
        raise NotImplementedError("Este método debe ser implementado por las subclases.")

    def atacar(self, enemigo):
        daño = max(0, self.calcular_daño(enemigo))
        enemigo.recibir_daño(daño)
        print(f"{self.nombre} inflige {daño} puntos de daño a {enemigo.nombre}.")


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, arma):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.arma = arma

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"  Arma: {self.arma}")

    def calcular_daño(self, enemigo):
        return (self.fuerza + self.arma) - enemigo.defensa


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, hechizo):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.hechizo = hechizo

    def mostrar_atributos(self):
        super().mostrar_atributos()
        print(f"  Hechizo: {self.hechizo}")

    def calcular_daño(self, enemigo):
        return (self.inteligencia * self.hechizo) - enemigo.defensa


def iniciar_combate(personaje1, personaje2):
    turno = 1
    while personaje1.esta_vivo() and personaje2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        print(f"{personaje1.nombre} ataca a {personaje2.nombre}:")
        personaje1.atacar(personaje2)

        if personaje2.esta_vivo():
            print(f"{personaje2.nombre} ataca a {personaje1.nombre}:")
            personaje2.atacar(personaje1)

        turno += 1

    if personaje1.esta_vivo():
        print(f"\n¡{personaje1.nombre} gana el combate!")
    elif personaje2.esta_vivo():
        print(f"\n¡{personaje2.nombre} gana el combate!")
    else:
        print("\nEl combate termina en empate.")


# Creación de los personajes
guerrero = Guerrero("Arthas", fuerza=25, inteligencia=10, defensa=5, vida=120, arma=7)
mago = Mago("Merlín", fuerza=10, inteligencia=20, defensa=3, vida=100, hechizo=5)

# Mostrar atributos iniciales
print("Atributos iniciales:")
guerrero.mostrar_atributos()
mago.mostrar_atributos()

# Iniciar el combate
iniciar_combate(guerrero, mago)
