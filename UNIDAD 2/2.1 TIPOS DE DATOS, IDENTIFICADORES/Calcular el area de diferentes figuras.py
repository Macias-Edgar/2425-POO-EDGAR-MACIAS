# Programa para calcular el área de diferentes figuras geométricas.
# Este programa permite calcular el área de un círculo, un rectángulo y un triángulo,
# solicitando al usuario los datos necesarios y mostrando el resultado.
# Se usan diferentes tipos de datos como integer, float, string y boolean.

import math  # Importamos la biblioteca math para usar la constante pi y funciones matemáticas


# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo.
    Fórmula: área = pi * radio^2
    Parámetro:
    radio (float): El radio del círculo.

    Retorna:
    float: El área del círculo.
    """
    area_circulo = math.pi * radio ** 2
    return area_circulo


# Función para calcular el área de un rectángulo
def calcular_area_rectangulo(base, altura):
    """
    Calcula el área de un rectángulo.
    Fórmula: área = base * altura
    Parámetros:
    base (float): La base del rectángulo.
    altura (float): La altura del rectángulo.

    Retorna:
    float: El área del rectángulo.
    """
    area_rectangulo = base * altura
    return area_rectangulo


# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo.
    Fórmula: área = (base * altura) / 2
    Parámetros:
    base (float): La base del triángulo.
    altura (float): La altura del triángulo.

    Retorna:
    float: El área del triángulo.
    """
    area_triangulo = (base * altura) / 2
    return area_triangulo


# Función principal para interactuar con el usuario
def main():
    """
    Función principal que permite al usuario elegir una figura geométrica
    y calcula su área según los datos proporcionados.
    """
    print("¡Bienvenido al programa de cálculo de áreas!")

    # Solicitamos al usuario que elija una figura
    figura = input("¿Qué figura deseas calcular (círculo, rectángulo, triángulo)? ").strip().lower()

    # Validamos la entrada del usuario
    if figura == "círculo":
        radio = float(input("Introduce el radio del círculo (en cm): "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} cm es: {area:.2f} cm².")

    elif figura == "rectángulo":
        base = float(input("Introduce la base del rectángulo (en cm): "))
        altura = float(input("Introduce la altura del rectángulo (en cm): "))
        area = calcular_area_rectangulo(base, altura)
        print(f"El área del rectángulo con base {base} cm y altura {altura} cm es: {area:.2f} cm².")

    elif figura == "triángulo":
        base = float(input("Introduce la base del triángulo (en cm): "))
        altura = float(input("Introduce la altura del triángulo (en cm): "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo con base {base} cm y altura {altura} cm es: {area:.2f} cm².")

    else:
        print("Figura no reconocida. Por favor, elige entre círculo, rectángulo o triángulo.")
        return  # Termina el programa si la figura no es válida

    # Preguntamos si el usuario quiere calcular el área de otra figura
    otra_figura = input("¿Quieres calcular el área de otra figura? (sí/no): ").strip().lower()

    if otra_figura == "sí":
        main()  # Llamada recursiva a la función principal para reiniciar el proceso
    else:
        print("¡Gracias por usar el programa de cálculo de áreas! Hasta luego.")


# Llamada a la función principal para iniciar el programa
if __name__ == "__main__":
    main()
