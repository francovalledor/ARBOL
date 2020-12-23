class Arbol:
    """
    Arbol binario sencillo, con métodos y atributos mínimos
    """
    def __init__(self, valor = None):
        self.__izq = None
        self.__der = None
        self.valor = valor
        self.__padre = None

    @property
    def padre(self):
        return self.__padre

    @property
    def izq(self):
        return self.__izq
    
    @izq.setter
    def izq(self, nodo):
        if self.izq != None and self.izq.padre == self:
            self.izq.__padre = None

        if nodo != None:
            self.__izq = nodo
            nodo.__padre = self
        else:
            self.__izq = None


    @property
    def der(self):
        return self.__der
    
    @der.setter
    def der(self, nodo):
        if self.der != None and self.der.padre == self:
            self.der.__padre = None

        if nodo != None:
            self.__der = nodo
            nodo.__padre = self
        else:
            self.__der = None
    
    def __repr__(self):
        return str(self.valor)

    def es_hoja(self):
        return self.der == None and self.izq==None