from nodo import Nodo

class Arbol:
    def __init__(self):
        self.raiz = None

    def get_raiz(self):
        return self.raiz

    def in_orden(self, callback):
        self._in_orden(self.raiz, callback)

    def pos_orden(self, callback):
        self._pos_orden(self.raiz, callback)

    def pre_orden(self, callback):
        self._pre_orden(self.raiz, callback)

    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.raiz is None:
            self.raiz = nuevo_nodo
        else:
            self._insertar(self.raiz, nuevo_nodo)


    def busqueda_valor(self, valor):
        return self._busqueda(self.raiz, valor)

    # Métodos protegidos
    def _in_orden(self, raiz, callback):
        if raiz is not None:
            self._in_orden(raiz.ret_hijo_izq(), callback)
            callback(raiz.ret_dato())
            self._in_orden(raiz.ret_hijo_der(), callback)

    def _pos_orden(self, raiz, callback):
        if raiz is not None:
            self._pos_orden(raiz.ret_hijo_izq(), callback)
            self._pos_orden(raiz.ret_hijo_der(), callback)
            callback(raiz.ret_dato())

    def _pre_orden(self, raiz, callback):
        if raiz is not None:
            callback(raiz.ret_dato())
            self._pre_orden(raiz.ret_hijo_izq(), callback)
            self._pre_orden(raiz.ret_hijo_der(), callback)

    def _insertar(self, raiz, nuevo_nodo):
        if nuevo_nodo.ret_dato() < raiz.ret_dato():
            if raiz.ret_hijo_izq() is None:
                raiz.unir_con_izq(nuevo_nodo)
                nuevo_nodo.set_padre(raiz)
            else:
                self._insertar(raiz.ret_hijo_izq(), nuevo_nodo)
        elif nuevo_nodo.ret_dato() > raiz.ret_dato():
            if raiz.ret_hijo_der() is None:
                raiz.unir_con_der(nuevo_nodo)
                nuevo_nodo.set_padre(raiz)
            else:
                self._insertar(raiz.ret_hijo_der(), nuevo_nodo)

    def _busqueda(self, arbol, valor):
        if arbol is None:
            return None
        if arbol.ret_dato() == valor:
            return arbol
        elif valor < arbol.ret_dato():
            return self._busqueda(arbol.ret_hijo_izq(), valor)
        else:
            return self._busqueda(arbol.ret_hijo_der(), valor)
