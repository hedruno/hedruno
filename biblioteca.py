from arbol import Arbol

class Libro:
    def __init__(self, titulo, autor, disponible=True):
        self.titulo = titulo
        self.autor = autor
        self.disponible = disponible

    def __str__(self):
        return f"{self.titulo} por {self.autor} ({'Disponible' if self.disponible else 'No Disponible'})"

    def __eq__(self, otro):
        return self.titulo == otro.titulo

    def __lt__(self, otro):
        return self.titulo < otro.titulo

    def __le__(self, otro):
        return self.titulo <= otro.titulo

    def __gt__(self, otro):
        return self.titulo > otro.titulo

    def __ge__(self, otro):
        return self.titulo >= otro.titulo


class Biblioteca:
    def __init__(self):
        self.arbol = Arbol()

    def agregar_libro(self, titulo, autor):
        libro = Libro(titulo, autor)
        self.arbol.insertar(libro)

    def buscar_libro(self, titulo):
        libro_buscar = Libro(titulo, "")  # Crear un libro con solo el título
        nodo = self.arbol.busqueda_valor(libro_buscar)
        if nodo:
            return nodo.ret_dato()
        return None

    def reservar_libro(self, titulo):
        libro_buscar = Libro(titulo, "")  # Crear un libro con solo el título
        nodo = self.arbol.busqueda_valor(libro_buscar)
        if nodo and nodo.ret_dato().disponible:
            nodo.ret_dato().disponible = False
            return True
        return False

    def mostrar_libros(self):
        libros = []
        def callback(libro):
            libros.append(str(libro))
        self.arbol.in_orden(callback)
        return libros
