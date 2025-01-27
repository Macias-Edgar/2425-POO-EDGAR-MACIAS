class ConexionBaseDeDatos:
    # Constructor: inicializa los parámetros de conexión y "abre" la conexión
    def __init__(self, nombre_base_de_datos, usuario, contrasena):
        self.nombre_base_de_datos = nombre_base_de_datos
        self.usuario = usuario
        self.contrasena = contrasena
        self.conexion = None
        print(
            f"Constructor: Conectando a la base de datos '{self.nombre_base_de_datos}' con el usuario '{self.usuario}'.")

    # Método para simular la apertura de la conexión
    def conectar(self):
        if not self.conexion:
            # Aquí simulamos la conexión a una base de datos (en un caso real, usaríamos un driver de BD)
            self.conexion = f"Conexión a {self.nombre_base_de_datos} establecida con el usuario '{self.usuario}'."
            print(self.conexion)
        else:
            print("Ya está conectado a la base de datos.")

    # Método para simular la ejecución de una consulta
    def ejecutar_consulta(self, consulta):
        if self.conexion:
            print(f"Ejecutando consulta: {consulta}")
        else:
            print("Error: No hay conexión establecida con la base de datos.")

    # Destructor: cierra la conexión (simulada) al destruir el objeto
    def __del__(self):
        if self.conexion:
            print(f"Destructor: Cerrando la conexión a la base de datos '{self.nombre_base_de_datos}'.")
            self.conexion = None
        else:
            print("Destructor: No hay conexión para cerrar.")


# Uso de la clase ConexionBaseDeDatos
if __name__ == "__main__":
    # Crear una instancia de la clase ConexionBaseDeDatos
    db = ConexionBaseDeDatos("mi_base_de_datos", "admin", "1234")

    # Conectar a la base de datos
    db.conectar()

    # Ejecutar una consulta
    db.ejecutar_consulta("SELECT * FROM usuarios;")

    # El destructor se llamará automáticamente al final del programa, cerrando la "conexión".
