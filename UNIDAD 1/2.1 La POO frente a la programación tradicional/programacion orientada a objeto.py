# Definimos la clase 'Clima' para organizar los datos y métodos relacionados con el clima
class Clima:
    # El constructor de la clase, inicializa una lista vacía para almacenar las temperaturas
    def __init__(self):
        self.temperaturas = []  # Lista para almacenar las temperaturas de la semana

    # Método para ingresar las temperaturas de cada día de la semana
    def ingresar_temperaturas(self):
        # Bucle para ingresar la temperatura de cada uno de los 7 días
        for i in range(7):
            # Solicita al usuario ingresar la temperatura para el día (i+1)
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            # Añade la temperatura ingresada a la lista 'temperaturas'
            self.temperaturas.append(temperatura)

    # Método para calcular el promedio semanal de las temperaturas
    def calcular_promedio(self):
        # Devuelve el promedio de las temperaturas: suma de todas dividida entre 7
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal que organiza el flujo del programa
def main():
    # Se crea un objeto de la clase Clima, lo que permite acceder a sus métodos y atributos
    clima = Clima()
    # Llamamos al método para ingresar las temperaturas de la semana
    clima.ingresar_temperaturas()
    # Llamamos al método para calcular el promedio de las temperaturas de la semana
    promedio = clima.calcular_promedio()
    # Imprime el promedio semanal con dos decimales
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Condición para que el código se ejecute solo cuando el archivo se ejecute directamente
if __name__ == "__main__":
    main()  # Llamada a la función principal para ejecutar el programa
