from TDA_arbol import ArbolBinario
from random import randint


#EJ1
arbol = ArbolBinario()
for i in range(0,1000):
    arbol.insertar(randint(0,10000))
#EJ1.a
print("INORDEN")
arbol.mostrar_inorden()
print("-"*50)

print("PREORDEN")
arbol.mostrar_preorden()
print("-"*50)

print("POSTORDEN")
arbol.mostrar_postorden()
print("-"*50)


#EJ1.b
numero_azar = randint(0,10000)
print("-"*50)
print(f"el numero {numero_azar} ¿se encuentra en el arbol?")
print("Sí" if arbol.buscar(numero_azar) else "No")
