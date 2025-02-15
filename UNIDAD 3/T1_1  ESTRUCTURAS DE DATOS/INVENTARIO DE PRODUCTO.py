class Producto:
    """
    Representa un producto con ID único, nombre, cantidad y precio.
    """

    def __init__(self, id_producto, nombre, cantidad, precio):
        self.id_producto = id_producto  # ID único del producto
        self.nombre = nombre  # Nombre del producto
        self.cantidad = cantidad  # Cantidad en stock
        self.precio = precio  # Precio del producto

    def __str__(self):
        return f"ID: {self.id_producto} | Nombre: {self.nombre} | Cantidad: {self.cantidad} | Precio: ${self.precio:.2f}"


class Inventario:
    """
    Gestiona una lista de productos, permitiendo operaciones como añadir, eliminar, actualizar y buscar productos.
    """

    def __init__(self):
        self.productos = []  # Lista para almacenar los productos

    def añadir_producto(self, producto):
        """Añade un producto al inventario si el ID es único."""
        if any(p.id_producto == producto.id_producto for p in self.productos):
            print("Error: El ID del producto ya existe.")
        else:
            self.productos.append(producto)
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id_producto):
        """Elimina un producto por su ID."""
        self.productos = [p for p in self.productos if p.id_producto != id_producto]
        print("Producto eliminado si existía.")

    def actualizar_producto(self, id_producto, nueva_cantidad=None, nuevo_precio=None):
        """Actualiza la cantidad o el precio de un producto dado su ID."""
        for producto in self.productos:
            if producto.id_producto == id_producto:
                if nueva_cantidad is not None:
                    producto.cantidad = nueva_cantidad
                if nuevo_precio is not None:
                    producto.precio = nuevo_precio
                print("Producto actualizado correctamente.")
                return
        print("Error: Producto no encontrado.")

    def buscar_producto(self, nombre):
        """Busca productos por nombre (puede haber coincidencias parciales)."""
        encontrados = [p for p in self.productos if nombre.lower() in p.nombre.lower()]
        return encontrados if encontrados else "No se encontraron productos con ese nombre."

    def mostrar_inventario(self):
        """Muestra todos los productos en el inventario."""
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos:
                print(producto)


def menu():
    """
    Interfaz de usuario en consola para gestionar el inventario.
    """
    inventario = Inventario()

    while True:
        print("\n--- Sistema de Gestión de Inventarios ---")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto")
        print("5. Mostrar inventario")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("Ingrese ID único del producto: ")
            nombre = input("Ingrese nombre del producto: ")
            cantidad = int(input("Ingrese cantidad del producto: "))
            precio = float(input("Ingrese precio del producto: "))
            inventario.añadir_producto(Producto(id_producto, nombre, cantidad, precio))

        elif opcion == "2":
            id_producto = input("Ingrese ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("Ingrese ID del producto a actualizar: ")
            nueva_cantidad = input("Nueva cantidad (deje vacío si no desea cambiar): ")
            nuevo_precio = input("Nuevo precio (deje vacío si no desea cambiar): ")

            nueva_cantidad = int(nueva_cantidad) if nueva_cantidad else None
            nuevo_precio = float(nuevo_precio) if nuevo_precio else None

            inventario.actualizar_producto(id_producto, nueva_cantidad, nuevo_precio)

        elif opcion == "4":
            nombre = input("Ingrese nombre del producto a buscar: ")
            resultado = inventario.buscar_producto(nombre)
            if isinstance(resultado, list):
                for p in resultado:
                    print(p)
            else:
                print(resultado)

        elif opcion == "5":
            inventario.mostrar_inventario()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    menu()
