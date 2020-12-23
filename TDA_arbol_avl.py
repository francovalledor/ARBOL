from TDA_arbol import ArbolBinario

class ArbolAVL(ArbolBinario):
    """Arbol Binario Balanceado"""
    def __init__(self, valor=None, padre=None):
        super().__init__(valor, padre)

    @property
    def factor_equilibrio(self):
        alt_izq = self.izq.altura if self.izq else 0
        alt_der = self.der.altura if self.der else 0
        return alt_der - alt_izq
    
    def __insertar(self, valor):
        if not self.valor:
            self.valor = valor
            return self
        elif valor == self.valor:
            return self
        elif valor > self.valor:
            if self.der:
                return self.der.insertar(valor)
            else:
                self.der = ArbolAVL(valor)
                return self.der
        else:
            if self.izq:
                return self.izq.insertar(valor)
            else:
                self.izq = ArbolAVL(valor)
                return self.izq
        
    def insertar(self, valor):
        """Inserta un valor y devuelve el arbol resultante"""
        nuevo_nodo = self.__insertar(valor)
        while (nuevo_nodo != None):
            if nuevo_nodo.factor_equilibrio == 2 and nuevo_nodo.der.factor_equilibrio == 1:
                self.__estrategia1(nuevo_nodo)
            if nuevo_nodo.factor_equilibrio == 2 and nuevo_nodo.der.factor_equilibrio == -1:
                self.__estrategia1(nuevo_nodo)
            if nuevo_nodo.factor_equilibrio == -2 and nuevo_nodo.izq.factor_equilibrio == -1:
                self.__estrategia2(nuevo_nodo)
            if nuevo_nodo.factor_equilibrio == -2 and nuevo_nodo.izq.factor_equilibrio == 1:
                self.__estrategia3(nuevo_nodo)
            if nuevo_nodo.padre != None:
                nuevo_nodo = nuevo_nodo.padre
            else:
                nuevo_nodo = None

        return self.raiz


    def __estrategia1(self, nodo):
        """
        docstring
        """
        menor = nodo
        mayor = menor.der

        if menor.padre != None:
            if menor.padre.der == menor:
                menor.padre.der = mayor
            else:
                menor.padre.izq = mayor

        menor.der = mayor.izq
        mayor.izq = menor


    def __estrategia2(self, nodo):
        """
        docstring
        """
        mayor = nodo
        menor = mayor.izq

        if mayor.padre != None:
            if mayor.padre.der == mayor:
                mayor.padre.der = menor
            else:
                mayor.padre.izq = menor

        mayor.izq = menor.der
        menor.der = mayor


    def __estrategia3(self, nodo):
        """
        docstring
        """
        mayor = nodo
        menor = mayor.izq
        medio = menor.der

        if mayor.padre != None:
            if mayor.padre.der == mayor:
                mayor.padre.der = medio
            else:
                mayor.padre.izq = medio

        menor.der = medio.izq
        medio.izq = menor
        mayor.izq = medio.der
        medio.der = mayor
