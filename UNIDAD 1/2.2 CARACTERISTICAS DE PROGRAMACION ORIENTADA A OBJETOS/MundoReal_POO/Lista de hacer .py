# Clase Tarea
class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

    def marcar_completada(self):
        self.completada = True
        print(f"Tarea '{self.descripcion}' marcada como completada.")

    def __str__(self):
        estado = "✔️" if self.completada else "❌"
        return f"{estado} {self.descripcion}"


# Clase Lista de Tareas
class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)
        print(f"Tarea '{tarea.descripcion}' agregada.")

    def mostrar_tareas(self):
        print("\nLista de Tareas:")
        for tarea in self.tareas:
            print(tarea)

    def completar_tarea(self, descripcion):
        for tarea in self.tareas:
            if tarea.descripcion == descripcion and not tarea.completada:
                tarea.marcar_completada()
                return
        print(f"Tarea '{descripcion}' no encontrada o ya completada.")


# Ejemplo de uso
lista = ListaTareas()
lista.agregar_tarea(Tarea("Estudiar Python"))
lista.agregar_tarea(Tarea("Hacer ejercicio"))
lista.mostrar_tareas()

lista.completar_tarea("Estudiar Python")
lista.mostrar_tareas()
