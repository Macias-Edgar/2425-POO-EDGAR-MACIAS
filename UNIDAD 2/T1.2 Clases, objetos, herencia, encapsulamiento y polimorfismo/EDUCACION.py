# Definimos una clase base llamada "Persona"
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self.__edad = edad   # Atributo privado (encapsulado)

    # Método público para acceder a la edad
    def obtener_edad(self):
        return self.__edad

    # Método público para modificar la edad de forma controlada
    def establecer_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            raise ValueError("La edad debe ser un número positivo.")

    # Método que será sobrescrito (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.nombre} y tengo {self.__edad} años."

# Definimos una clase derivada llamada "Estudiante"
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)  # Llamamos al constructor de la clase base
        self.grado = grado

    # Sobrescritura del método "presentarse" (polimorfismo)
    def presentarse(self):
        return f"Hola, soy {self.nombre}, tengo {self.obtener_edad()} años y estudio en el grado {self.grado}."

# Definimos otra clase derivada llamada "Profesor"
class Profesor(Persona):
    def __init__(self, nombre, edad, asignatura):
        super().__init__(nombre, edad)
        self.asignatura = asignatura

    # Sobrescritura del método "presentarse"
    def presentarse(self):
        return f"Hola, soy el profesor {self.nombre}, tengo {self.obtener_edad()} años y enseño {self.asignatura}."

# Instancias de las clases para demostrar el uso
persona = Persona("Carlos", 40)
estudiante = Estudiante("Ana", 15, "10mo año")
profesor = Profesor("Luis", 50, "Matemáticas")

# Uso de encapsulación: obtener y establecer edad
print(persona.presentarse())
print(f"Edad actual de Carlos: {persona.obtener_edad()} años")
persona.establecer_edad(41)
print(f"Edad actualizada de Carlos: {persona.obtener_edad()} años")

# Polimorfismo: llamada al método "presentarse"
print(estudiante.presentarse())
print(profesor.presentarse())
