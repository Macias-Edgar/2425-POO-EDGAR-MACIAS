# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    # Lista que almacenará las temperaturas diarias
    temperaturas = []
    for i in range(7):  # Se pide la temperatura para cada uno de los 7 días
        # Solicita al usuario ingresar la temperatura para el día i+1
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        # Añade la temperatura ingresada a la lista de temperaturas
        temperaturas.append(temperatura)
    return temperaturas  # Devuelve la lista con las temperaturas ingresadas

# Función para calcular el promedio de las temperaturas semanales
def calcular_promedio(temperaturas):
    # Calcula el promedio sumando todas las temperaturas y dividiendo por 7 (el número de días)
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    # Llamamos a la función ingresar_temperaturas para obtener los datos de los 7 días
    temperaturas = ingresar_temperaturas()
    # Llamamos a la función calcular_promedio para obtener el promedio de las temperaturas
    promedio = calcular_promedio(temperaturas)
    # Imprime el promedio semanal de las temperaturas, con dos decimales
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

# Condición para que el código se ejecute solo cuando el archivo se ejecute directamente, no cuando se importe
if __name__ == "__main__":
    main()  # Llamamos a la función principal para ejecutar el programa
