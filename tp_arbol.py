from TDA_arbol import ArbolBinario
from TDA_arbol_expresion import ArbolExpresion
from TDA_arbol_simple import Arbol as ArbolSimple
from pokemondata import ArbolPokemon
from utils.contador import Contador
from random import randint

# # #EJ1
# # arbol = ArbolBinario()
# # for i in range(0,1000):
# #     arbol.insertar(randint(0,10000))
# # #EJ1.a
# # print("INORDEN")
# # arbol.mostrar_inorden()
# # print("-"*50)

# # print("PREORDEN")
# # arbol.mostrar_preorden()
# # print("-"*50)

# # print("POSTORDEN")
# # arbol.mostrar_postorden()
# # print("-"*50)


# # #EJ1.b
# # numero_azar = randint(0,10000)
# # print("-"*50)
# # print(f"el numero {numero_azar} ¿se encuentra en el arbol?")
# # print("Sí" if arbol.buscar(numero_azar) else "No")

# # # #EJ1.c
# # # borrados = 0
# # # while borrados < 3:
# # #     numero_azar = randint(0,10000)
# # #     if arbol.buscar(numero_azar):
# # #         arbol.borrar(numero_azar)
# # #         borrados += 1

# # #EJ1.d
# # print('La altura del subarbol derecho es {}'.format(arbol.der.altura))
# # print('La altura del subarbol izquierdo es {}'.format(arbol.izq.altura))


# # #EJ1.e
# # # Determinar si existen valores repetidos en el árbol.
# # # No existen valores repetidos en el arbol por la definición del TDA
# # # Cuando se quiere insertar un valor que ya se encuentra en el arbol
# # # este directamente no se inserta.


# # contador = {}
# # contador['pares'] = 0
# # contador['impares'] = 0


# # def contar_pares_impares(arbol):
# #     if arbol.valor % 2 == 0:
# #         contador['pares'] += 1
# #     else:
# #         contador['impares'] += 1

# # arbol.inorden(contar_pares_impares)
# # print('Hay {} pares y {} impares'.format(contador['pares'], contador['impares']))

# # #EJ2
# # expresion = '(2*(6+3)*5*(2/2))'
# # arbol = ArbolExpresion(expresion)
# # print(arbol)
# # print('RESULTADO: ', arbol.resolver())

# # expresion = '6*8+7/2+1-6'
# # arbol = ArbolExpresion(expresion)
# # print(arbol)
# # print('RESULTADO: ', arbol.resolver())

# #EJ3
# # Conseguir material sobre transformada de Knuth

# #EJ4
# # Implementar un algoritmo que contemple dos funciones, 
# # la primera que devuelva el hijo derecho de un nodo y
# # la segunda que devuelva el hijo izquierdo.
# # Resuelto en el TDA

# # #EJ5
# # from TDA_arbol_avl import ArbolAVL as Arbol

# # from marvel import personajes, Personaje

# # arbol = Arbol()
# # for personaje in personajes:
# #     arbol = arbol.insertar(personaje)
# # print('En Orden Alfabético')
# # arbol.mostrar_inorden()

# # print('-'*120)
# # print('\n'*2)

# # def mostrar_villanos(nodo):
# #     personaje = nodo.valor
# #     if personaje.es_villano():
# #         print(personaje)
# # print('Mostrar Villanos')
# # arbol.inorden(mostrar_villanos)
# # print('-'*120)
# # print('\n'*2)

# # def mostrar_heroes_con_c(nodo):
# #     personaje = nodo.valor
# #     if personaje.es_heroe() and personaje.nombre[0] == 'C':
# #         print(personaje)
# # print('Heroes con C')
# # arbol.inorden(mostrar_heroes_con_c)
# # print('-'*120)
# # print('\n'*2)

# # def cantidad_heroes(nodo):
# #     personaje = nodo.valor
# #     if personaje.es_heroe():
# #         Contador.inc()

# # contador.reset()
# # arbol.inorden(cantidad_heroes)
# # print('Cantidad de heroes: {}'.format(Contador.get()))
# # print('-'*120)
# # print('\n'*2)



# # #Doctor strange mal cargado. Borro el anterior y cargo uno nuevo
# # print('CORREGIR DOCTOR STRANGE')
# # arbol.borrar(Personaje('DOCTOR STRAGE'))
# # arbol = arbol.insertar(Personaje('DOCTOR STRANGE'))
# # arbol.mostrar_inorden()
# # print('-'*120)
# # print('\n'*2)


# # def mostrar_heroes(nodo):
# #     personaje = nodo.valor
# #     if personaje.es_heroe():
# #         print(personaje)

# # print('antiorden')
# # arbol.antiorden(mostrar_heroes)
# # print('-'*120)
# # print('\n'*2)


# # #BOSQUE
# # heroes = Arbol()
# # villanos = Arbol()
# # for personaje in personajes:
# #     if personaje.es_heroe():
# #         heroes = heroes.insertar(personaje)
# #     else:
# #         villanos = villanos.insertar(personaje)

# # print('Hay {heroes} heroes y {villanos} villanos'.format(heroes=heroes.cantidad_nodos, villanos=villanos.cantidad_nodos))


# # print('HEROES:')
# # heroes.mostrar_inorden()

# # print('\nVILLANOS:')
# # villanos.mostrar_inorden()


# #EJ 7 Minimo y máximo
# from TDA_arbol_avl import ArbolAVL as Arbol
# from random import randint
# arbol = Arbol()

# for i in range(1,20):
#     arbol = arbol.insertar(randint(1,101))

# def print_max(arbol):
#     nodo = arbol
#     while nodo.der != None:
#         nodo = nodo.der

#     print('El máximo es {}'.format(nodo.valor))

# def print_min(arbol):
#     nodo = arbol
#     while nodo.izq != None:
#         nodo = nodo.izq

#     print('El mínimo es {}'.format(nodo.valor))

# print_max(arbol)
# print_min(arbol)


# #EJ8 Ver TDA_Arbol_Huffman.py


# #EJ9
# from random import randint
# arbol = ArbolBinario()
# for i in range(1, 20):
#     arbol.insertar(randint(0,1000))
# print(arbol)
# def esta_lleno_el_nivel(nivel, arbol):
#     diferencia = arbol.nodos_de_un_nivel(nivel) - arbol.cuantos_nodos_hay_en_el_nivel(nivel)
#     if diferencia == 0:
#         print(f"El nivel {nivel} está lleno")
#     else:
#         print(f"Al nivel {nivel} le faltan {diferencia} nodos para completarse")

# esta_lleno_el_nivel(1, arbol)
# esta_lleno_el_nivel(2, arbol)
# esta_lleno_el_nivel(3, arbol)
# esta_lleno_el_nivel(4, arbol)


# # EJ10
# # 10.a resuelto en el TDA
# from random import randint
# arbol = ArbolBinario()
# for i in range(1, 20):
#     arbol.insertar(randint(0,1000))
# print(arbol)
# print(f"El arbol tiene {arbol.cantidad_nodos} nodos")


# # 10.b
# def si_es_hoja_inc(nodo):
#     if nodo.es_hoja():
#         Contador.inc()
# Contador.reset()
# arbol.inorden(si_es_hoja_inc)
# cantidad_hojas = Contador.total
# print(f"El arbol tiene {cantidad_hojas} hojas")

# # 10.c
# # arbol.mostrar_inorden()


# # 10.d
# # Cada nodo tiene una referencia a su padre. En el caso de la raiz padre=None.

# # 10.e
# print(f"La altura del arbol es {arbol.altura}")


# 11. Generar un árbol binario que tenga nueve niveles, luego diseñar los algoritmos necesarios
# para resolver las siguientes actividades:

# from random import randint
# arbol = ArbolBinario()
# while arbol.altura < 10:
#     arbol.insertar(randint(1,100000))


# # 11.a a. Generar un bosque cortando los tres primeros niveles del árbol
# bosque = []

# def agregar_arboles_al_bosque(nodo):
#     if nodo.nivel == 3:
#         bosque.append(nodo)
# arbol.inorden(agregar_arboles_al_bosque)
# print(f"hay {len(bosque)} arboles en el bosque")

# # 11.b Contar cuantos nodos tiene cada árbol del bosque
# index = 1
# for arbol in bosque:
#     arbol.padre = None
#     print(f"El arbol nro {index} tiene {arbol.cantidad_nodos} nodos")
#     index += 1

# # 11.c Realizar un barrido preorden de cada árbol del bosque
# index = 1
# for arbol in bosque:
#     print('='*80)
#     print(f"Arbon {index}")
#     print('='*80)
#     arbol.mostrar_preorden()
#     index += 1

# # 11.d Determinar cuál es el árbol con mayor cantidad de nodos
# index = 1
# nro_arbol = 0
# max = 0
# for arbol in bosque:
#     if arbol.cantidad_nodos > max:
#         nro_arbol = index
#         max = arbol.cantidad_nodos
#     index += 1
# print(f"El arbol con mayor numero de nodos es el nro {nro_arbol}, que tiene {max} nodos")

# # 11.e Indicar que árboles del bosque están llenos
# index = 1
# for arbol in bosque:
#     if arbol.es_lleno():
#         print(f"El arbol {index} está lleno")
#         print(arbol)
#     index += 1

# 12 ver arbol_shield.py

# 13 ver morse.py

# 15 Una empresa de nano satélites dedicada al monitoreo de lotes campo destinados al agro...
# Variable            Símbolo         Frecuencia       Caracter Asignado
# Estado del clima
#                     Despejado       0.22              'D'
#                     Nublado         0.15              'N'
#                     Lluvia          0.03              'L'

# Humedad del suelo
#                     Baja            0.26              'B'
#                     Alta            0.14              'A'

# Código de identificación 1 
#                     1               0.05              '1'
#                     2               0.01              '2'

# Código de identificación 2 
#                     3               0.035             '3'
#                     5               0.06              '5'

# Código de identificación 3 
#                     7               0.02              '7'
#                     8               0.025             '8'


# frecuencias = {}
# frecuencias['D'] = 0.22
# frecuencias['N'] = 0.15
# frecuencias['L'] = 0.03
# frecuencias['B'] = 0.26
# frecuencias['A'] = 0.14
# frecuencias['1'] = 0.05
# frecuencias['2'] = 0.01
# frecuencias['3'] = 0.035
# frecuencias['5'] = 0.06
# frecuencias['7'] = 0.02
# frecuencias['8'] = 0.025

# from TDA_Arbol_Huffman import Huffman

# msj = ''
# for caracter, frecuencia in frecuencias.items():
#     msj += caracter*int(frecuencia*1000)

# diccionario = Huffman(msj).diccionario

# print('Usar los siguientes codigos para enviar los datos:')
# print(diccionario)

# mensaje_original = 'NubladoBaja157'
# msj_a_cifrar = 'NB157'
# print('Mensaje Original:')
# print(msj_a_cifrar)


# msj_cifrado = Huffman.cifrar(msj_a_cifrar, diccionario)
# print('Mensaje Cifrado:')
# print(msj_cifrado)

# msj_descifrado = Huffman.descifrar(msj_cifrado, diccionario)
# print('Mensaje Descifrado:')
# print(msj_descifrado)

# print(f"Tamaño mensaje original {len(mensaje_original.encode('utf-8'))*8} bits")
# print(f"Tamaño mensaje cifrado {len(msj_cifrado)} bits")



# # 16 (ver pokemondata.py)

# # 19 Estados del tiempo
# arbolClima = ArbolSimple()
# class ReglaClima:
#     def __init__(self, nombre, umbral):
#         self.nombre = nombre
#         self.umbral = umbral
    
#     def __repr__(self):
#         return f"{self.nombre}: {self.umbral}"

# #Condiciones
# visibilidad = 'visibilidad'
# viento = 'viento'
# humedad = 'humedad'
# presion = 'presion'

# #Estados
# despejado = 'despejado'
# nublado = 'nublado'
# parcial_nublado = 'parcialmente nublado'
# mayor_nublado = 'mayormente nublado'
# lluvia = 'lluvia'


# #### CARGANDO EL ARBOL DE DECISION
# arbolClima.valor = ReglaClima(visibilidad, 15)
# arbolClima.der = ArbolSimple(despejado)
# arbolClima.izq = ArbolSimple(ReglaClima(humedad, 70))
# nodohumedad = arbolClima.izq
# nodohumedad.izq = ArbolSimple(ReglaClima(viento, 8.7))
# nodohumedad.der = ArbolSimple(ReglaClima(visibilidad, 8))

# viento87 = nodohumedad.izq
# viento87.der = ArbolSimple(parcial_nublado)
# viento87.izq = ArbolSimple(ReglaClima(viento, 5))
# viento5 = viento87.izq
# viento5.der = ArbolSimple(nublado)
# viento5.izq = ArbolSimple(despejado)

# visibilidad8 = nodohumedad.der
# visibilidad8.izq = ArbolSimple(ReglaClima(presion, 1013))
# visibilidad8.der = ArbolSimple(ReglaClima(humedad, 92))

# presion1013 = visibilidad8.izq
# presion1013.izq = ArbolSimple(ReglaClima(humedad, 96))
# presion1013.der = ArbolSimple(ReglaClima(viento, 7.2))

# humedad96 = presion1013.izq
# humedad96.der = ArbolSimple(mayor_nublado)
# humedad96.izq = ArbolSimple(nublado)

# viento72 = presion1013.der
# viento72.der = ArbolSimple(nublado)
# viento72.izq = ArbolSimple(ReglaClima(presion, 1018))

# presion1018 = viento72.izq
# presion1018.der = ArbolSimple(nublado)
# presion1018.izq = ArbolSimple(ReglaClima(visibilidad, 1))
# visibilidad1 = presion1018.izq
# visibilidad1.der = ArbolSimple(mayor_nublado)
# visibilidad1.izq = ArbolSimple(lluvia)

# humedad92 = visibilidad8.der
# humedad92.izq = ArbolSimple(ReglaClima(visibilidad, 12))
# humedad92.der = ArbolSimple(ReglaClima(viento, 12.2))

# visibilidad12 = humedad92.izq
# visibilidad12.izq = ArbolSimple(despejado)
# visibilidad12.der = ArbolSimple(mayor_nublado)

# viento122 = humedad92.der
# viento122.izq = ArbolSimple(lluvia)
# viento122.der = ArbolSimple(nublado)



# ### DECIDIDOR
# def determinar_estado(registro, arbol_decision):
#     while not arbol_decision.es_hoja():
#         nombre = arbol_decision.valor.nombre
#         umbral = arbol_decision.valor.umbral
#         if registro[nombre] > umbral:
#             arbol_decision = arbol_decision.der
#         else:
#             arbol_decision = arbol_decision.izq

#     return arbol_decision.valor


# # REGISTRO AL AZAR
# registro = {}
# registro[visibilidad] = randint(0,20)
# registro[humedad] = randint(0,100)
# registro[viento] = randint(0,20)
# registro[presion] = randint(884,1078)


# # ESTADO DEL TIEMPO
# print(f"Si ", end='')
# for nombre, valor in registro.items():
#     print(f"{nombre} es {valor}, ", end='')
# print(f"el estado del tiempo es {determinar_estado(registro, arbolClima).upper()}.")
    
    

# # 21
# class Criatura:
#     def __init__(self, nombre):
#         self.nombre = nombre.lower()
#         self.derrotado_por = None
#         self.descripcion = None

#     def mostrar_info(self):
#             print( f"{self.nombre.upper()}{(' fue derrotado por ' + str(self.derrotado_por).upper()) if self.derrotado_por else '' }")
#             print(f"\t {self.descripcion if self.descripcion else ''} \n")
    

#     def __repr__(self):
#         return f"{self.nombre.upper()}{(' fue derrotado por ' + str(self.derrotado_por.nombre).upper()) if self.derrotado_por else '' }\n\t {self.descripcion if self.descripcion else ''} \n "

#     def __eq__(self, otro):
#         if type(otro) == type(None):
#             return False

#         if type(otro) == str:
#             return self.nombre == otro.lower()
#         else:
#             return self.nombre == otro.nombre.lower()

#     def __lt__(self, otro):
#         if type(otro) == str:
#             return self.nombre < otro.lower()
#         else:
#             return self.nombre < otro.nombre.lower()

#     def __gt__(self, otro):
#         if type(otro) == str:
#             return self.nombre > otro.lower()
#         else:
#             return self.nombre > otro.nombre.lower()


# ## CRIATURAS
# criaturas = {}
# criaturas['ceto'] = Criatura('ceto')
# criaturas['tifon'] = Criatura('tifon')
# criaturas['equidna'] = Criatura('equidna')
# criaturas['dino'] = Criatura('dino')
# criaturas['pefredo'] = Criatura('pefredo')
# criaturas['enio'] = Criatura('enio')
# criaturas['escila'] = Criatura('escila')
# criaturas['caribdis'] = Criatura('caribdis')
# criaturas['euriale'] = Criatura('euriale')
# criaturas['esteno'] = Criatura('esteno')
# criaturas['medusa'] = Criatura('medusa')
# criaturas['ladon'] = Criatura('ladon')
# criaturas['aguila'] = Criatura('aguila del caucaso')
# criaturas['quimera'] = Criatura('quimera')
# criaturas['hidra'] = Criatura('hidra de lerna')
# criaturas['leon'] = Criatura('leon de nemea')
# criaturas['esfinge'] = Criatura('esfinge')
# criaturas['dragon'] = Criatura('dragon de la colquida')
# criaturas['cerbero'] = Criatura('cerbero')
# criaturas['cerda'] = Criatura('cerda de cromion')
# criaturas['ortro'] = Criatura('ortro')
# criaturas['toro'] = Criatura('toro de creta')
# criaturas['jabali_calidon'] = Criatura('jabali de calidon')
# criaturas['carcinos'] = Criatura('carcinos')
# criaturas['gerion'] = Criatura('gerion')
# criaturas['cloto'] = Criatura('cloto')
# criaturas['laquesis'] = Criatura('laquesis')
# criaturas['atropos'] = Criatura('atropos')
# criaturas['minotauro'] = Criatura('minotauro de creta')
# criaturas['harpias'] = Criatura('harpias')
# criaturas['argos'] = Criatura('argos panoptes')
# criaturas['aves'] = Criatura('aves del estinfalo')
# criaturas['talos'] = Criatura('talos')
# criaturas['sirenas'] = Criatura('sirenas')
# criaturas['piton'] = Criatura('piton')
# criaturas['cierva'] = Criatura('cierva de cerinea')
# criaturas['basilisco'] = Criatura('basilisco')
# criaturas['jabali'] = Criatura('jabali de erimanto')
# criaturas['zeus'] = Criatura('zeus')
# criaturas['perseo'] = Criatura('perseo')
# criaturas['heracles'] = Criatura('heracles')
# criaturas['belerofonte'] = Criatura('belerofonte')
# criaturas['edipo'] = Criatura('edipo')
# criaturas['teseo'] = Criatura('teseo')
# criaturas['hermes'] = Criatura('hermes')
# criaturas['medea'] = Criatura('medea')
# criaturas['apolo'] = Criatura('apolo')


# ## DERROTAS
# criaturas['tifon'].derrotado_por = criaturas['zeus']
# criaturas['equidna'].derrotado_por = criaturas['argos']
# criaturas['medusa'].derrotado_por = criaturas['perseo']
# criaturas['ladon'].derrotado_por = criaturas['heracles']
# criaturas['quimera'].derrotado_por = criaturas['belerofonte']
# criaturas['hidra'].derrotado_por = criaturas['heracles']
# criaturas['leon'].derrotado_por = criaturas['heracles']
# criaturas['esfinge'].derrotado_por = criaturas['edipo']
# criaturas['cerda'].derrotado_por = criaturas['teseo']
# criaturas['ortro'].derrotado_por = criaturas['heracles']
# criaturas['minotauro'].derrotado_por = criaturas['teseo']
# criaturas['argos'].derrotado_por = criaturas['hermes']
# criaturas['talos'].derrotado_por = criaturas['medea']
# criaturas['piton'].derrotado_por = criaturas['apolo']



# class ArbolCriaturas(ArbolPokemon):
#     def __init__(self, valor=None):
#         super().__init__(valor)

#     def insertar(self, valor):
#         """Inserta un nuevo nodo en el arbol y devuelve una referencia a ese nodo"""
#         if not self.valor:
#             self.valor = valor
#         elif valor == self.valor:
#             pass #Lanzar una exepcion o hacer algo
#         elif valor > self.valor:
#             if self.der:
#                 self.der.insertar(valor)
#             else:
#                 self.der = ArbolCriaturas(valor)
#         else:
#             if self.izq:
#                 self.izq.insertar(valor)
#             else:
#                 self.izq = ArbolCriaturas(valor) 
    
#     def buscar(self, valor):
#         """
#         Devuelve nodo si el valor se encuentra en el arbol,
#         None en caso contrario
#         """
#         if type(self.valor) == type(None):
#             return None
#         elif self.valor == valor:
#             return self
#         elif self.valor > valor:
#             if not self.izq:
#                 return None
#             else:
#                 return self.izq.buscar(valor)
#         else:
#             if not self.der:
#                 return None
#             else:
#                 return self.der.buscar(valor)


#     def borrar(self, valor):
#         """Borra un elemento del arbol (si existe), sino no hace nada"""
#         nodo_a_borrar = self.buscar(valor)
        
#         if type(nodo_a_borrar) == type(None):
#             raise Exception('El valor que intenta eliminar no se encuentra en el arbol')
#         else:
#             if nodo_a_borrar.es_hoja():
#                 nodo_a_borrar.valor = None
#             elif self.__tiene_un_solo_hijo(nodo_a_borrar):   # Si tiene un solo hijo se elimina 
#                                                     # el nodo actual y se reemplaza por el hijo
#                 if type(nodo_a_borrar.der) != type(None):
#                     nodo_hijo = nodo_a_borrar.der
#                 else:
#                     nodo_hijo = nodo_a_borrar.izq
            
#                 # "nodo" es hijo derecho o izquierdo?
#                 if nodo_a_borrar.padre != None:   
#                     if nodo_a_borrar.padre.der == nodo_a_borrar:
#                         nodo_a_borrar.padre.der = nodo_hijo
#                     else:
#                         nodo_a_borrar.padre.izq = nodo_hijo

#                     nodo_a_borrar.valor = None
            
#             else: # el nodo tiene ambos hijos
#                 el_mayor_de_los_menores = nodo_a_borrar.izq

#                 while (type(el_mayor_de_los_menores.der) != type(None)):
#                     el_mayor_de_los_menores = el_mayor_de_los_menores.der
                

#                 aux = el_mayor_de_los_menores.izq

#                 if el_mayor_de_los_menores.padre.der == el_mayor_de_los_menores:
#                     el_mayor_de_los_menores.padre.der = aux
#                 else:
#                     el_mayor_de_los_menores.padre.izq = aux
                
#                 if nodo_a_borrar.padre.der == nodo_a_borrar:
#                     nodo_a_borrar.padre.der = el_mayor_de_los_menores
#                 else:
#                     nodo_a_borrar.padre.izq = el_mayor_de_los_menores

#                 el_mayor_de_los_menores.izq = nodo_a_borrar.izq
#                 el_mayor_de_los_menores.der = nodo_a_borrar.der


#     def __tiene_un_solo_hijo(self, nodo):
#         return ((type(nodo.der) != type(None)) or (type(nodo.izq) != type(None))) and not ((type(nodo.der) != (type(None))) and (type(nodo.izq) != type(None)))

# arbol_criaturas = ArbolCriaturas() 

# for criatura in criaturas.values():
#     arbol_criaturas.insertar(criatura)


# def mostrar_inorden(nodo):
#     print(nodo.valor)

# arbol_criaturas.inorden(mostrar_inorden)

# ### MOSTRAR INFO DE TALOS
# talos = arbol_criaturas.buscar('talos')
# print(talos)



# # Determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas
# contador_victorias = {}
# def computar_victorias(nodo):
#     criatura = nodo.valor
#     if criatura.derrotado_por != None:
#         if contador_victorias.get(criatura.derrotado_por.nombre) is not None:
#             contador_victorias[criatura.derrotado_por.nombre] += 1
#         else:
#             contador_victorias[criatura.derrotado_por.nombre] = 1

# arbol_criaturas.inorden(computar_victorias)

# for i in range(0,3):
#     criatura_mayor = ''
#     victorias_mayor = 0

#     for criatura, victorias in contador_victorias.items():
#         if victorias > victorias_mayor:
#             victorias_mayor = victorias
#             criatura_mayor = criatura
#     del contador_victorias[criatura_mayor]
#     print(f"El {i+1}º en victorias es {criatura_mayor} con {victorias_mayor} victorias")


# # Listar las criaturas derrotadas por Heracles
# def mostrar_derrotada_por_heracles(nodo):
#     criatura = nodo.valor
#     if (
#         criatura != None 
#         and criatura.derrotado_por != None
#         and criatura.derrotado_por.nombre.lower() == 'heracles'
#         ):
        
#         print(criatura)

# print('-'*120)
# print("DERROTADOS POR HERACLES")
# print('-'*120)
# arbol_criaturas.inorden(mostrar_derrotada_por_heracles)


# # Listar las criaturas que no han sido derrotadas
# def mostrar_no_derrotadas(nodo):
#     criatura = nodo.valor
#     if (
#         criatura != None 
#         and criatura.derrotado_por == None
#         ):
        
#         print(criatura)

# print('-'*120)
# print("NO DERROTADAS")
# print('-'*120)
# arbol_criaturas.inorden(mostrar_no_derrotadas)


# # Eliminar al Basilisco y a las Sirenas
# arbol_criaturas.borrar('basilisco')
# arbol_criaturas.borrar('sirenas')

# nodo_ladon = arbol_criaturas.buscar('ladon')
# print(nodo_ladon)
# nodo_ladon.valor.nombre = 'dragon ladon'
# print(nodo_ladon)



### EJ 22
diccionario = {
    '1111': 'R',
    '111011': ',',
    '111010': 'V',
    '11100': 'U',
    '110': ' ',
    '10111': 'S',
    '10110': 'P',
    '10101': 'C',
    '101001': 'B',
    '101000': 'Q',
    '100': 'E',
    '0111': 'O',
    '01101': 'T',
    '01100': 'M',
    '01011': 'G',
    '01010': 'D',
    '0100': 'N',
    '0011': 'L',
    '0010': 'I',
    '000': 'A'
    }

# Un diccionario podría ser el anterior. 
# He hecho el diccionario con el algoritmo de TDA_Arbol_Huffman.py
# Lo he corregido en excel.
# Lo he hecho a mano
# Lo he hecho con un software online
# No pude descifrar nada legible