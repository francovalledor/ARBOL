try:
    from binarytree import Node
except:
    pass

class ArbolBinario:
    """Crea un arbol binario"""
    def __init__(self, valor=None, padre=None):
        self.__izq = None
        self.__der = None
        self.valor = valor
        self.der = None
        self.izq = None
        self.padre = padre

    @property
    def izq(self):
        return self.__izq

    @izq.setter
    def izq(self, nodo):
        if self.izq != None and self.izq.padre == self:
            self.izq.padre = None

        if nodo != None:
            self.__izq = nodo
            nodo.padre = self
        else:
            self.__izq = None

    @property
    def der(self):
        return self.__der

    @der.setter
    def der(self, nodo):
        if self.der != None and self.der.padre == self:
            self.der.padre = None
            
        if nodo != None:
            self.__der = nodo
            nodo.padre = self
        else:
            self.__der = None

    def es_vacio(self):
        """Devuelve true si el arbol es vacío, sino false"""
        return not self.raiz.valor

    def es_hoja(self):
        """Devuelve true si el arbol es vacío, sino false"""
        return (not self.der) and (not self.izq)

    def insertar(self, valor):
        """Inserta un nuevo nodo en el arbol y devuelve una referencia a ese nodo"""
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

    def _get_nodo(self, valor):
        """
        Devuelve ArbolBinario si el valor se encuentra en el arbol,
        None en caso contrario
        """
        if not self.valor:
            return None
        elif self.valor == valor:
            return self
        elif self.valor > valor:
            if not self.izq:
                return None
            else:
                return self.izq._get_nodo(valor)
        else:
            if not self.der:
                return None
            else:
                return self.der._get_nodo(valor)


    def mostrar_inorden(self):
        if not self.valor:
            return None
        else:
            if self.izq:
                self.izq.mostrar_inorden()
            
            print(self.valor)

            if self.der:
                self.der.mostrar_inorden()


    def mostrar_antiorden(self):
        if not self.valor:
            return None
        else:
            if self.der:
                self.der.mostrar_antiorden()
            
            print(self.valor)

            if self.izq:
                self.izq.mostrar_antiorden()


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
        """
        Aplica una función a cada nodo del árbol en INORDEN
        """
        if not self.valor:
            return None
        else:
            if self.izq:
                self.izq.inorden(funcion)
            
            funcion(self)

            if self.der:
                self.der.inorden(funcion)


    def preorden(self, funcion):
        """
        Aplica una función a cada nodo del árbol en PREORDEN
        """
        if not self.valor:
            return None
        else:
            funcion(self)

            if self.izq:
                self.izq.preorden(funcion)

            if self.der:
                self.der.preorden(funcion)


    def postorden(self, funcion):
        """
        Aplica una función a cada nodo del árbol en POSTORDEN
        """
        if not self.valor:
            return None
        else:
            if self.izq:
                self.izq.postorden(funcion)


            if self.der:
                self.der.postorden(funcion)

            funcion(self)

    def antiorden(self, funcion):
        """
        Aplica una función a cada nodo del árbol en orden inverso al inorden
        """
        if not self.valor:
            return None
        else:
            if self.der:
                self.der.antiorden(funcion)

            funcion(self)

            if self.izq:
                self.izq.antiorden(funcion)



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
            return self.der.es_lleno() and self.izq.es_lleno()
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

    def borrar(self, valor):
        """Borra un elemento del arbol (si existe), sino no hace nada"""
        nodo_a_borrar = self._get_nodo(valor)
        
        if type(nodo_a_borrar) == type(None):
            raise Exception('El valor que intenta eliminar no se encuentra en el arbol')
        else:
            if nodo_a_borrar.es_hoja():
                nodo_a_borrar.valor = None
            elif self.__tiene_un_solo_hijo(nodo_a_borrar):   # Si tiene un solo hijo se elimina 
                                                    # el nodo actual y se reemplaza por el hijo
                if type(nodo_a_borrar.der) != type(None):
                    nodo_hijo = nodo_a_borrar.der
                else:
                    nodo_hijo = nodo_a_borrar.izq
            
                # "nodo" es hijo derecho o izquierdo?
                if nodo_a_borrar.padre != None:   
                    if nodo_a_borrar.padre.der == nodo_a_borrar:
                        nodo_a_borrar.padre.der = nodo_hijo
                    else:
                        nodo_a_borrar.padre.izq = nodo_hijo

                    nodo_a_borrar.valor = None
            
            else: # el nodo tiene ambos hijos
                el_mayor_de_los_menores = nodo_a_borrar.izq

                while (type(el_mayor_de_los_menores.der) != type(None)):
                    el_mayor_de_los_menores = el_mayor_de_los_menores.der
                

                aux = el_mayor_de_los_menores.izq

                if el_mayor_de_los_menores.padre.der == el_mayor_de_los_menores:
                    el_mayor_de_los_menores.padre.der = aux
                else:
                    el_mayor_de_los_menores.padre.izq = aux
                
                if nodo_a_borrar.padre.der == nodo_a_borrar:
                    nodo_a_borrar.padre.der = el_mayor_de_los_menores
                else:
                    nodo_a_borrar.padre.izq = el_mayor_de_los_menores

                el_mayor_de_los_menores.izq = nodo_a_borrar.izq
                el_mayor_de_los_menores.der = nodo_a_borrar.der


    @property
    def profundidad(self):
        """Profundidad de este arbol"""
        return self.altura()


    def get_dir_nodo(self, valor, dir_actual=''):
        """
        Devuelve la direccion del nodo que contenga el valor buscado o None


        La direccion está formada por letras "i" (para izquierda)
        y letras "d" para derecha. Por ejemplo la direccion "diid" hace referencia 
        al elemento que está desde la raiz, un nodo a la derecha, dos nodos a la 
        izquierda y un nodo a la derecha.
        Otro ejemplo, "ddi" sería dos nodos a la derecha y un nodo a la izquierda.

        Para hacer más eficiente la direccion se podría usar numeros binarios que 
        comiencen en 1: "diid" podría ser 11001. (el uno más a la izquierda no se 
        debe tener en cuenta a la hora de direccionar)
        """
        if not self.valor:
            return None
        elif self.valor == valor:
            return dir_actual
        elif self.valor > valor:
            if not self.izq:
                return None
            else:
                return self.izq.get_dir_nodo(valor, dir_actual=dir_actual+'i')
        else:
            if not self.der:
                return None
            else:
                return self.der.get_dir_nodo(valor, dir_actual=dir_actual+'d')

    @property
    def nivel(self):
        """
        Devuelve el nivel del nodo actual
        """
        if self.padre == None:
            return 0
        else:
            return 1 + self.padre.nivel

    @staticmethod
    def nodos_de_un_nivel(nivel):
        return 2**nivel

    def cuantos_nodos_hay_en_el_nivel(self, nivel):
        if self.raiz.altura < nivel + 1:
            return 0
        elif self.nivel == nivel:
            return 1
        elif self.nivel < nivel:
            contador = 0
            if self.der != None:
                contador += self.der.cuantos_nodos_hay_en_el_nivel(nivel)
            if self.izq != None:
                contador += self.izq.cuantos_nodos_hay_en_el_nivel(nivel)
            return contador
        else:
            return 0

    def __tiene_un_solo_hijo(self, nodo):
        return ((type(nodo.der) != type(None)) or (type(nodo.izq) != type(None))) and not ((type(nodo.der) != (type(None))) and (type(nodo.izq) != type(None)))


    def __repr__(self):
        return '{valor}'.format(valor=self.valor)
    
    def __to_binary_tree(self):
        try:
            raiz = Node(self.valor)
            if self.der:
                raiz.right = self.der.__to_binary_tree()

            if self.izq:
                raiz.left = self.izq.__to_binary_tree()

            return raiz
        except NameError:
            return "Impresion no disponible, por favor instale binarytree (pip install binarytree)"

    def __str__(self):
        return str(self.__to_binary_tree())

