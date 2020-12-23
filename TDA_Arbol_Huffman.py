from TDA_arbol_simple import Arbol

class NodoHuffman(Arbol):
    def __init__(self, valor = None):
        super().__init__(valor)
        self.caracter = None

    def get_diccionario_coordenadas(self, diccionario=None, coord_actual=''):
        if diccionario == None:
            diccionario = dict()

        if self.es_hoja():
            if coord_actual != '' and self.valor != None:
                diccionario[coord_actual] = self.caracter
        else:
            if self.der != None:
                self.der.get_diccionario_coordenadas(diccionario=diccionario, coord_actual=coord_actual+'1')
            if self.izq != None:
                self.izq.get_diccionario_coordenadas(diccionario=diccionario, coord_actual=coord_actual+'0')

        return diccionario



class Huffman:
    def __init__(self, mensaje):
        self.mensaje_original = mensaje
        self.diccionario = dict()
        self.arbol = None
        self.__crear_arbol()

    def __contar_apariciones(self, mensaje):
        apariciones = dict()
        for caracter in mensaje:
            if caracter in apariciones:
                apariciones[caracter] += 1
            else:
                apariciones[caracter] = 1

        return apariciones

    def __crear_arbol(self):
        if len(self.mensaje_original)<1:
            raise Exception('El mensaje no puede ser vacío')
        apariciones = self.__contar_apariciones(self.mensaje_original)

        def sortByValue(nodo):
            return nodo.valor

        lista_caracteres = []
        for caracter, peso in apariciones.items():
            nodo = NodoHuffman(peso)
            nodo.caracter = caracter
            lista_caracteres.append(nodo)

        lista_caracteres.sort(key=sortByValue)

        while len(lista_caracteres)>1:
            nodo1 = lista_caracteres[0]
            del lista_caracteres[0]
            nodo2 = lista_caracteres[0]
            del lista_caracteres[0]
            suma = nodo1.valor + nodo2.valor
            nodo_union = NodoHuffman(suma)
            nodo_union.izq = nodo1
            nodo_union.der = nodo2
            lista_caracteres.append(nodo_union)
            lista_caracteres.sort(key=sortByValue)
        self.arbol = lista_caracteres[0]
        self.diccionario = self.arbol.get_diccionario_coordenadas()

    @staticmethod    
    def cifrar(msj, diccionario):
        diccionario_inverso = dict()
        for clave, valor in diccionario.items():
            diccionario_inverso[valor] = clave
        diccionario = diccionario_inverso

        resultado = ''
        alimentador = ''
        while len(msj) > 0:
            alimentador += msj[0]
            msj = msj[1:]
            if alimentador in diccionario:
                resultado += diccionario[alimentador]
                alimentador = ''
        
        # resultado devuelve un string que representa numeros binarios.
        # para visualizarlos de forma más sencilla.
        return resultado  

    @staticmethod
    def descifrar(msj, diccionario):
        resultado = ''
        alimentador = ''
        while len(msj) > 0:
            alimentador += msj[0]
            msj = msj[1:]
            if alimentador in diccionario:
                resultado += diccionario[alimentador]
                alimentador = ''
        
        return resultado

    @staticmethod
    def tasa_ahorro(msj, msj_cifrado):
        len_cifrado = len(msj_cifrado)/8
        len_original = len(msj.encode('utf-8'))
        return len_cifrado/len_original


####### DESCOMENTAR
# msj1 = """Arbol binario es aquel en el que cada nodo tiene como máximo el grado 2. Un árbol binario es equilibrado cuando la diferen-
# cia de altura entre los subárboles de cualquier nodo es como máximo una unidad. Cuando los subárboles de todos los nodos
# tienen todos la misma altura se dice que está perfectamente equilibrado.
# Árbol binario completo es un árbol equilibrado en el que todos los nodos interiores, es decir aquellos con descendientes,
# tienen dos hijos. Un árbol binario completo de profundidad n para cada nivel, del 0 al nivel n-1 tiene un conjunto lleno de
# nodos y todos los nodos hoja a nivel n ocupan las posiciones más a la izquierda del árbol. Un árbol binario completo que con-
# tiene 2n nodos a nivel n es un árbol lleno.
# Un árbol binario lleno tiene todas sus hojas al mismo nivel y sus nodos interiores tienen cada uno dos hijos. Cuando un
# árbol binario es lleno es, necesariamente, completo. Un árbol binario completo es equilibrado, mientras que un árbol binario
# lleno es totalmente equilibrado."""

# msj2 = "este es un mensaje corto"

# msj3 = 'qazwsxedcrfvtgbyhnujmik,ol.pñ-´`+¡0987665531!"·$%&/()=' #sin repeticiones

# msj4 = """Implementar las rutinas necesarias para la gestión de un archivo binario para control de personal cuyos registros están for-
# mados por los campos DNI (campo clave), nombre del empleado, departamento y sueldo. Se desea acceder a los registros
# directamente por su clave mediante el empleo de una función hash. El archivo se diseñará para contener 100 registros (más
# un 27% para colisiones). Utilice una función hash aritmética modular y el método de exploración lineal para la resolu-
# ción de colisiones.
# Análisis
# El ejercicio es análogo al anterior y sólo levemente modificado para que trabaje en memoria externa. El archivo se abre de
# forma que si no existe se crea y si existe permite la adición de nuevos datos. La creación del archivo implica su apertura en
# el modo “wb+” y la inicialización de MaxReg posiciones marcando el campo ocupado como libre (L). Puesto que por el
# método de transformación de claves a registros con claves distintas puede corresponderles la misma posición (colisiones),
# el campo ocupado será consultado cuando se vayan a efectuar altas con la finalidad de no sobreescribir información exis-
# tente. Si en la posición devuelta por la función hash no se ha escrito nunca, o los datos que allí aparecen están borrados
# (campo ocupado con una L o una B) se coloca en ella la nueva información, pero si dicha posición está ocupada se efectúa
# una búsqueda secuencial hasta encontrar una posición válida. Para borrar un registro se marca su campo ocupado con una
# B. Se incluye un programa principal simplificado para mostrar el funcionamiento del programa."""

# msj5 = """
# qwertyuiopàsdfghjklñ´zxcvbnm,.1234567890'¡'?¿ºª¿?=)(/&%$·"!ª)<>
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
# """

# msj6 = "\u03A9\u0394\u03C3\u03BC\u03B5\u00B0\u220F"  ##Caracteres unicode de 3 bytes y 4 bytes

# msj7 = "abc"*80  ##Solo 3 caracteres


# msjs = [msj1, msj2, msj3, msj4, msj5, msj6, msj7]

# i = 1
# for msj in msjs:
#     diccionario = Huffman(msj).diccionario
#     cifrado = Huffman.cifrar(msj, diccionario)
#     tasa = Huffman.tasa_ahorro(msj, cifrado)
#     print("Tasa de compresion msj{i}: {tasa:1.0f}%".format(i=i, tasa=(1-tasa)*100))
#     i += 1

####### FIN DESCOMENTAR




# La tasa de compresión está comparada a UTF-8.
# Conclusiones: 
#   -la tasa de compresión mejora si hay una distribución no uniforme de caracteres, donde hay caracteres 
# que aparecen mucho más que otros. (ver msj5).
# 
#   -la tasa de compresión empeora si la distribución de aparaciones es equilibrada y cada caracter tiene
# aproximadamente el mismo peso ponderado que los demás.  (ver msj3)
# 
#   -Mientras menor es la cantidad de caracteres usados menor es la longitud de la clave. Y por ende mayor es la 
# tasa de compresion. Si en el mensaje solo se usan 2 caracteres las claves tendran una longitud de 1 (ver msj7).
#   
#   -En el caso de usar caracteres unicode de 3 o 4 bytes la tasa de compresion es muy alta (ver msj6)
# 
# En el calculo de la tasa de ahorro no está contemplado el peso del diccionario. El diccionario debe viajar junto 
# con el mensaje cifrado.
# Se puede usar un solo diccionario para cifrar varios mensajes pero hay que tener en cuenta 
# algunas cuestiones:
#   -El diccionario debe contener todos los caracteres que se quieran usar en los mensajes
#   -El diccionario no será el óptimo para cada mensaje.