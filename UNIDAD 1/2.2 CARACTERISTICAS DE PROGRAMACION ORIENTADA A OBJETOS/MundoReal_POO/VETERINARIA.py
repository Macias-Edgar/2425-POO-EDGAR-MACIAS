# Clase Mascota
class Mascota:
    def __init__(self, nombre, especie, edad):
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.historial = []

    def agregar_tratamiento(self, tratamiento):
        self.historial.append(tratamiento)
        print(f"Tratamiento '{tratamiento}' agregado al historial de {self.nombre}.")

    def __str__(self):
        return f"{self.nombre} ({self.especie}, {self.edad} años) - Tratamientos: {len(self.historial)}"


# Clase Veterinaria
class Veterinaria:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mascotas = []

    def registrar_mascota(self, mascota):
        self.mascotas.append(mascota)
        print(f"Mascota '{mascota.nombre}' registrada en {self.nombre}.")

    def mostrar_mascotas(self):
        print("\nMascotas Registradas:")
        for mascota in self.mascotas:
            print(mascota)


# Ejemplo de uso
veterinaria = Veterinaria("Clínica Animal Macias")
mascota1 = Mascota("Max", "Perro", 5)
mascota2 = Mascota("sol", "Gato", 3)

veterinaria.registrar_mascota(mascota1)
veterinaria.registrar_mascota(mascota2)

mascota1.agregar_tratamiento("Vacuna Antirrábica")
mascota2.agregar_tratamiento("Desparasitación")

veterinaria.mostrar_mascotas()
