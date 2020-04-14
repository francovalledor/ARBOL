from TDA_arbol import ArbolBinario
from random import randint

arbol = ArbolBinario()

for i in range(0,100):
    arbol.insertar(randint(0,1000))

arbol.mostrar_inorden()