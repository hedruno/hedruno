# nodo.py
class Nodo:
    def __init__(self, dato, padre=None):
        self.dato = dato
        self.padre = padre
        self.hijo_izq = None
        self.hijo_der = None

    def ret_dato(self):
        return self.dato

    def ret_hijo_izq(self):
        return self.hijo_izq

    def ret_hijo_der(self):
        return self.hijo_der

    def set_dato(self, dato):
        self.dato = dato

    def unir_con_izq(self, nodo):
        self.hijo_izq = nodo

    def unir_con_der(self, nodo):
        self.hijo_der = nodo

    def set_padre(self, nodo):
        self.padre = nodo

    def get_padre(self):
        return self.padre
