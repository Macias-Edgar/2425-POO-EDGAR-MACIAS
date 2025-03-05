# Clase que representa un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, categoria, isbn):
        self.info = (autor, titulo)  # Tupla para atributos inmutables (autor y título)
        self.categoria = categoria  # La categoría sí puede cambiar
        self.isbn = isbn  # Identificador único del libro

    def __str__(self):
        return f"{self.info[1]} de {self.info[0]} (Categoría: {self.categoria}, ISBN: {self.isbn})"


# Clase que representa a un usuario de la biblioteca
class Usuario:
    def __init__(self, nombre, user_id):
        self.nombre = nombre
        self.user_id = user_id  # ID único del usuario
        self.libros_prestados = []  # Lista de libros actualmente prestados

    def __str__(self):
        return f"Usuario: {self.nombre} (ID: {self.user_id})"


# Clase principal que gestiona la biblioteca
class Biblioteca:
    def __init__(self):
        self.libros_disponibles = {}  # Diccionario con ISBN como clave y objeto Libro como valor
        self.usuarios_registrados = set()  # Conjunto para IDs de usuario únicos
        self.historial_prestamos = {}  # Diccionario que relaciona usuario con libros prestados

    # Método para agregar un libro a la biblioteca
    def agregar_libro(self, libro):
        if libro.isbn not in self.libros_disponibles:
            self.libros_disponibles[libro.isbn] = libro
            print(f"Libro agregado: {libro}")
        else:
            print("Este libro ya existe en la biblioteca.")

    # Método para quitar un libro de la biblioteca
    def quitar_libro(self, isbn):
        if isbn in self.libros_disponibles:
            eliminado = self.libros_disponibles.pop(isbn)
            print(f"Libro eliminado: {eliminado}")
        else:
            print("El libro no se encuentra en la biblioteca.")

    # Método para registrar un usuario en la biblioteca
    def registrar_usuario(self, usuario):
        if usuario.user_id not in self.usuarios_registrados:
            self.usuarios_registrados.add(usuario.user_id)
            self.historial_prestamos[usuario.user_id] = usuario  # Se guarda el objeto usuario
            print(f"Usuario registrado: {usuario}")
        else:
            print("Este usuario ya está registrado.")

    # Método para dar de baja a un usuario
    def dar_de_baja_usuario(self, user_id):
        if user_id in self.usuarios_registrados:
            self.usuarios_registrados.remove(user_id)
            self.historial_prestamos.pop(user_id, None)  # Se elimina el usuario del historial
            print(f"Usuario con ID {user_id} dado de baja.")
        else:
            print("El usuario no está registrado.")

    # Método para prestar un libro a un usuario
    def prestar_libro(self, user_id, isbn):
        if user_id in self.usuarios_registrados and isbn in self.libros_disponibles:
            usuario = self.historial_prestamos[user_id]
            libro = self.libros_disponibles.pop(isbn)  # Se remueve de los libros disponibles
            usuario.libros_prestados.append(libro)  # Se añade a la lista de libros prestados del usuario
            print(f"Libro '{libro.info[1]}' prestado a {usuario.nombre}.")
        else:
            print("No se pudo prestar el libro. Verifique usuario y disponibilidad del libro.")

    # Método para devolver un libro
    def devolver_libro(self, user_id, isbn):
        if user_id in self.usuarios_registrados:
            usuario = self.historial_prestamos[user_id]
            for libro in usuario.libros_prestados:
                if libro.isbn == isbn:
                    usuario.libros_prestados.remove(libro)  # Se elimina de la lista de libros prestados
                    self.libros_disponibles[isbn] = libro  # Se regresa a la biblioteca
                    print(f"Libro '{libro.info[1]}' devuelto por {usuario.nombre}.")
                    return
            print("El usuario no tiene este libro prestado.")
        else:
            print("Usuario no registrado.")

    # Método para buscar libros por título, autor o categoría
    def buscar_libros(self, criterio, valor):
        encontrados = [libro for libro in self.libros_disponibles.values() if valor.lower() in str(libro).lower()]
        if encontrados:
            print("Libros encontrados:")
            for libro in encontrados:
                print(libro)
        else:
            print("No se encontraron libros que coincidan con la búsqueda.")

    # Método para listar libros prestados de un usuario
    def listar_libros_prestados(self, user_id):
        if user_id in self.usuarios_registrados:
            usuario = self.historial_prestamos[user_id]
            if usuario.libros_prestados:
                print(f"Libros prestados a {usuario.nombre}:")
                for libro in usuario.libros_prestados:
                    print(libro)
            else:
                print(f"{usuario.nombre} no tiene libros prestados.")
        else:
            print("Usuario no registrado.")


# ---------------- PRUEBAS DEL SISTEMA ---------------- #

# Crear la biblioteca
biblioteca = Biblioteca()

# Crear libros
libro1 = Libro("El Señor de los Anillos", "J.R.R. Tolkien", "Fantasía", "35978")
libro2 = Libro("El Hobbit", "J.R.R. Tolkien", "Fantasía", "67890")

# Agregar libros a la biblioteca
biblioteca.agregar_libro(libro1)
biblioteca.agregar_libro(libro2)

# Crear usuarios
usuario1 = Usuario("Ana Paula", "U001")
usuario2 = Usuario("Felipe Ordoñez", "U002")

# Registrar usuarios en la biblioteca
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

# Prestar libros
biblioteca.prestar_libro("U001", "35978")
biblioteca.prestar_libro("U002", "67890")

# Listar libros prestados
biblioteca.listar_libros_prestados("U001")
biblioteca.listar_libros_prestados("U002")

# Devolver libros
biblioteca.devolver_libro("U001", "12345")
biblioteca.devolver_libro("U002", "67890")

# Buscar libros
biblioteca.buscar_libros("titulo", "Anillos")