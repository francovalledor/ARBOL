try:
    from graphviz import Digraph, nohtml
except:
    pass

# class Nodo:
#     def __init__(self, valor):
#         self.valor = valor
#         self.izq = None
#         self.der = None
    

class ArbolBinario:
    def __init__(self, valor=None, padre=None):
        """Crea un arbol binario"""
        self.valor = valor
        self.der = None
        self.izq = None
        self.padre = padre

    def es_vacio(self):
        """Devuelve true si el arbol es vacío, sino false"""
        return not self.raiz.valor

    def insertar(self, valor):
        """Inserta un nuevo nodo en el arbol"""
        if not self.valor:
            self.valor = valor
        elif valor == self.valor:
            pass #Lanzar una exepcion o hacer algo
        elif valor > self.valor:
            if self.der:
                self.der.insertar(valor)
            else:
                self.der = ArbolBinario(valor, padre=self)
        else:
            if self.izq:
                self.izq.insertar(valor)
            else:
                self.izq = ArbolBinario(valor, padre=self)

    def buscar(self, valor)->bool:
        """
        Devuelve True si el valor se encuentra en el arbol,
        False en caso contrario
        """
        if not self.valor:
            return False
        elif self.valor == valor:
            return True
        elif self.valor > valor:
            if not self.izq:
                return False
            else:
                return self.izq.buscar(valor)
        else:
            if not self.der:
                return False
            else:
                return self.der.buscar(valor)


    def mostrar_inorden(self):
        if not self.valor:
            return None
        else:
            if self.izq:
                self.izq.mostrar_inorden()
            print(self.valor)

            if self.der:
                self.der.mostrar_inorden()


    def mostrar_preorden(self):
        if not self.valor:
            return None
        else:
            print(self.valor)
            if self.izq:
                self.izq.mostrar_preorden()

            if self.der:
                self.der.mostrar_preorden()

    def mostrar_postorden(self):
        if not self.valor:
            return None
        else:
            if self.izq:
                self.izq.mostrar_postorden()

            if self.der:
                self.der.mostrar_postorden()

            print(self.valor)


    def inorden(self, funcion):
        if not self.valor:
            return None
        else:
            if self.izq:
                self.izq.inorden(funcion)

            funcion(self)

            if self.der:
                self.der.inorden(funcion)


    def preorden(self, funcion):
        if not self.valor:
            return None
        else:
            funcion(self)

            if self.izq:
                self.izq.preorden(funcion)


            if self.der:
                self.der.preorden(funcion)


    def postorden(self, funcion):
        if not self.valor:
            return None
        else:
            if self.izq:
                self.izq.postorden(funcion)


            if self.der:
                self.der.postorden(funcion)

            funcion(self)


    @property
    def raiz(self):
        """Nodo raiz"""
        raiz = self
        while raiz.padre:
            raiz = raiz.padre

        return raiz

    @property
    def altura(self):
        """Altura del arbol"""
        if not self.valor:
            return 0
        else:
            alt_der = self.der.altura if self.der else 0
            alt_izq = self.izq.altura if self.izq else 0
                
            return 1 + max([alt_der, alt_izq])

    def es_lleno(self):
        """Devuelve verdadero si es un arbol lleno"""
        if not self.valor: 
            return True
        elif (not self.der) and (not self.izq):
            return True
        elif (self.der) and (self.izq):
            return True and self.der.es_lleno() and self.izq.es_lleno()
        else: 
            return False

    @property
    def cantidad_nodos(self):
        if not self.valor:
            return 0
        else:
            cant_izq = self.izq.cantidad_nodos if self.izq else 0
            cant_der = self.der.cantidad_nodos if self.der else 0
            return 1 + cant_der + cant_izq

    def borrar(self):
        """Borra un elemento del arbol"""
        pass

    def pertenece(self):
        """Determina si un elemento pertenece al arbol"""
        pass

    @property
    def profundidad(self):
        """Profundidad de este arbol"""
        pass

    
    def mostrarme(self):
        try:
            dot = Digraph
            nh = nohtml
        except:
            print('Para mostrar se necesita la libreria "graphviz"')

