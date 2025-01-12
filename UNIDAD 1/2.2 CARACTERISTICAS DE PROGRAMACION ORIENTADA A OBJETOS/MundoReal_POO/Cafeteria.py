# Clase Cafetera
class Cafetera:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima
        self.nivel_agua = capacidad_maxima

    def preparar_cafe(self, tipo, cantidad):
        if self.nivel_agua >= cantidad:
            self.nivel_agua -= cantidad
            print(f"Preparando {tipo}... ¡Listo! ☕")
        else:
            print("No hay suficiente agua. Llena el depósito.")

    def rellenar_agua(self):
        self.nivel_agua = self.capacidad_maxima
        print("Depósito de agua lleno.")

    def estado(self):
        print(f"Nivel de agua: {self.nivel_agua} ml / {self.capacidad_maxima} ml")


# Ejemplo de uso
cafetera = Cafetera(1000)  # Capacidad de 1000 ml

cafetera.estado()
cafetera.preparar_cafe("Espresso", 200)
cafetera.preparar_cafe("Capuchino", 300)
cafetera.estado()
cafetera.rellenar_agua()
cafetera.estado()
