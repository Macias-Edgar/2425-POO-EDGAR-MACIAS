import os

def mostrar_codigo(ruta_script):
    ruta_script_absoluta = os.path.abspath(ruta_script)
    try:
        with open(ruta_script_absoluta, 'r', encoding='utf-8') as archivo:
            print(f"\n--- Código de {os.path.basename(ruta_script)} ---\n")
            print(archivo.read())
    except FileNotFoundError:
        print("El archivo no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error al leer el archivo: {e}")

def mostrar_menu():
    ruta_base = os.path.dirname(os.path.abspath(__file__))

    opciones = {
        '1': os.path.join("UNIDAD 1", "1.2 TECNICA DE PROGRAMACION", "TECNICA DE PROGRAMACION.py"),
        '2': os.path.join("UNIDAD 1", "2.1 La POO frente a la programación tradicional", "programacion orientada a objeto.py"),
        '3': os.path.join("UNIDAD 1", "2.1 La POO frente a la programación tradicional", "programacion tradicional.py"),
        '4': os.path.join("UNIDAD 1", "2.2 CARACTERISTICAS DE PROGRAMACION ORIENTADA A OBJETOS", "MundoReal_POO", "Cafeteria.py"),
        '5': os.path.join("UNIDAD 1", "2.2 CARACTERISTICAS DE PROGRAMACION ORIENTADA A OBJETOS", "MundoReal_POO", "Lista de hacer .py"),
        '6': os.path.join("UNIDAD 1", "2.2 CARACTERISTICAS DE PROGRAMACION ORIENTADA A OBJETOS", "MundoReal_POO", "VETERINARIA.py"),
        '7': os.path.join("UNIDAD 2", "2.1 TIPOS DE DATOS, IDENTIFICADORES", "Calcular el area de diferentes figuras.py"),
        '8': os.path.join("UNIDAD 2", "T1.2 Clases, objetos, herencia, encapsulamiento y polimorfismo", "EDUCACION.py"),
        '9': os.path.join("UNIDAD 2", "T1.3 Constructores y Destructores", "Conexion de base de datos.py"),
    }

    while True:
        print("\n******** Menu Principal - Dashboard *************")
        for key, value in opciones.items():
            print(f"{key} - {value}")
        print("0 - Salir")

        eleccion = input("Elige un script para ver su código o '0' para salir: ")
        if eleccion == '0':
            break
        elif eleccion in opciones:
            ruta_script = os.path.join(ruta_base, opciones[eleccion])
            mostrar_codigo(ruta_script)
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    mostrar_menu()
