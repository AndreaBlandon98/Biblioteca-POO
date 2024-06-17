class Libro:
    def __init__(self, titulo, autor, isbn, disponibilidad=True):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponibilidad = disponibilidad

    def prestar_libro(self):
        if self.disponibilidad:
            self.disponibilidad = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' no está disponible en este momento.")

class Biblioteca:
    def __init__(self):
        self.lista_libros = []

    def agregar_libro(self, libro):
        self.lista_libros.append(libro)
        print(f"El libro '{libro.titulo}' ha sido agregado a la biblioteca.")

    def mostrar_libros_disponibles(self):
        libros_disponibles = [libro for libro in self.lista_libros if libro.disponibilidad]
        if libros_disponibles:
            print("Libros disponibles en la biblioteca:")
            for libro in libros_disponibles:
                print(f"- {libro.titulo} by {libro.autor}")
        else:
            print("No hay libros disponibles en este momento en la biblioteca.")
