from TDA_arbol_avl import ArbolAVL as ArbolBinario


# arbol = ArbolBinario()
# from random import randint
# for i in range(1,50):
#     arbol = arbol.insertar(randint(1, 300))
# print(arbol)
# print('_'*130)


arbol = ArbolBinario()


for i in range(1,20):
    arbol = arbol.insertar(20-i)
    arbol = arbol.insertar(20+i)
    print(arbol)