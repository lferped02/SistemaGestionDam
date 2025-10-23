# Nombre: LiLi Fernández Pedrosa 
# Grupo: 2ºDAM 

# Clase Autor
class Autor:
    # Representa a la persona que ha escrito un libro.
    def __init__(self, nombre, apellidos):
        # Atributos: 
        # Nombre
        # Apellidos
        self.nombre = nombre
        self.apellidos = apellidos

    # Método: 
    # MostrarAutor: muestra el nombre completo del autor.
    def mostrar_autor(self):
        print("Autor:", self.nombre, self.apellidos)


# Clase Libro
class Libro:
    # Representa a un libro de la biblioteca 
    def __init__(self, titulo, isbn):
        # Atributos:
        # Título
        # ISBN
        # Autor (objeto de tipo Autor)
        self.titulo = titulo
        self.isbn = isbn
        self.autor = None  # Se asigna más tarde

    # Método:
    # AñadirAutor: asocia un autor al libro.
    def añadir_autor(self, autor):
        self.autor = autor

    # MostrarLibro: muestra la información completa del libro.
    def mostrar_libro(self):
        print("Título:", self.titulo)
        print("ISBN:", self.isbn)
        if self.autor:
            print("Autor:", self.autor.nombre, self.autor.apellidos)
        else:
            print("Autor: No asignado")
        print("------------------------")

    # ObtenerTítulo: devuelve el título del libro.
    def obtener_titulo(self):
        return self.titulo


# Clase Biblioteca
class Biblioteca:
    # Representa el conjunto de libros disponibles.
    def __init__(self):
        # Atributo:
        # istaLibros: lista que almacena todos los libros.
        self.lista_libros = []

    # Método:
    # NumeroLibros: devuelve el número total de libros registrados.
    def numero_libros(self):
        return len(self.lista_libros)

    # AñadirLibro: agrega un libro nuevo a la lista.
    def añadir_libro(self, libro):
        self.lista_libros.append(libro)

    # BorrarLibro: elimina un libro a partir de su título.
    def borrar_libro(self, titulo):
        for libro in self.lista_libros:
            if libro.titulo == titulo:
                self.lista_libros.remove(libro)
                print(f"Libro '{titulo}' eliminado.")
                return
        print(f"No se encontró el libro con título '{titulo}'.")

    # MostrarBiblioteca: muestra todos los libros que contiene.
    def mostrar_biblioteca(self):
        if not self.lista_libros:
            print("La biblioteca está vacía.")
        else:
            print("\nLibros en la biblioteca:")
            for libro in self.lista_libros:
                libro.mostrar_libro()


# Funciones del programa
# Además de las clases, el programa incluirá funciones para gestionar el flujo de trabajo:

# MostrarMenu: presenta las opciones al usuario.
def mostrar_menu():
    print("\n========= MENÚ DE BIBLIOTECA =========")
    print("1) Añadir libro")
    print("2) Mostrar biblioteca")
    print("3) Borrar libro")
    print("4) Número total de libros")
    print("5) Salir")

# AñadirLibroABiblioteca: gestiona la introducción de un nuevo libro, solicitando título, ISBN y autor.
def añadir_libro_a_biblioteca(biblioteca):
    print("\n--- Añadir nuevo libro ---")
    titulo = input("Título: ")
    isbn = input("ISBN: ")
    nombre_autor = input("Nombre del autor: ")
    apellidos_autor = input("Apellidos del autor: ")

    autor = Autor(nombre_autor, apellidos_autor)
    libro = Libro(titulo, isbn)
    libro.añadir_autor(autor)
    biblioteca.añadir_libro(libro)
    print("Libro añadido correctamente.")

# MostrarBiblioteca: muestra los libros registrados.
def mostrar_biblioteca(biblioteca):
    print("\n--- Libros registrados ---")
    biblioteca.mostrar_biblioteca()

# BorrarLibro: elimina un libro a partir de su título.
def borrar_libro(biblioteca):
    print("\n--- Borrar libro ---")
    titulo = input("Introduce el título del libro a borrar: ")
    biblioteca.borrar_libro(titulo)

# NumeroLibros: muestra la cantidad total de libros en la biblioteca.
def numero_libros(biblioteca):
    total = biblioteca.numero_libros()
    print(f"\nTotal de libros en la biblioteca: {total}")

# Programa principal
def ejecutar_biblioteca():
    mi_biblioteca = Biblioteca()

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ")

        if opcion == "1":
            añadir_libro_a_biblioteca(mi_biblioteca)
        elif opcion == "2":
            mostrar_biblioteca(mi_biblioteca)
        elif opcion == "3":
            borrar_libro(mi_biblioteca)
        elif opcion == "4":
            numero_libros(mi_biblioteca)
        elif opcion == "5":
            print("Fin del programa. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar el programa
ejecutar_biblioteca()
