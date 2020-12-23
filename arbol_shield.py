from TDA_arbol_simple import Arbol

arbol = Arbol()
raiz = arbol
arbol.valor = "Hay misión?"
arbol.der = Arbol("Entonces no es necesario elegir a nadie")

arbol.izq = Arbol("Es una misión intergaláctica?")
arbol = arbol.izq #Es una misión intergaláctica?
arbol.izq = Arbol("Guardianas de la Galaxia son los ideales")

arbol.der = Arbol("Es una misión de destruccion?")
arbol = arbol.der #Es una misión de destruccion?
arbol.izq = Arbol("Hulk es el ideal")

arbol.der = Arbol("Es necesario no ser detectado?")
arbol = arbol.der #Es necesario no ser detectado?
arbol.izq = Arbol("Ant-Man es el ideal")

arbol.der = Arbol("Es una misión de defensa y recuperación?")
arbol = arbol.der #Es una misión de defensa y recuperación?
arbol.izq = Arbol("El Capitan America es el ideal por ser un supersoldado de ética incorruptible")

arbol.der = Arbol("Es necesario viajar a otras galaxias?")
arbol = arbol.der #Es necesario viajar a otras galaxias?
arbol.izq = Arbol("Capitana Marvel es la ideal")

arbol.der = Arbol("Es necesario infiltrarse?")
arbol = arbol.der #Es necesario infiltrarse?
arbol.izq = Arbol("Black Widow es el ideal")

arbol.der = Arbol("Se necesita tecnología avanzada?")
arbol = arbol.der #Se necesita tecnología avanzada?
arbol.izq = Arbol("IronMan entiende mucho de eso")

arbol.der = Arbol("Es necesario moverse de un lugar a otro rápidamente?")
arbol = arbol.der #Es necesario moverse de un lugar a otro rápidamente?
arbol.izq = Arbol("Doctor Strange sí que sabe hacerlo")

arbol.der = Arbol("Hay que luchar contra grandes ejercitos?")
arbol = arbol.der #Hay que luchar contra grandes ejercitos?
arbol.izq = Arbol("Entonces Thor no debería faltar")

arbol = raiz

def consultar(arbol):
    while True:
        print(arbol.valor)
        if arbol.es_hoja():
            break
        respuesta = input('s/n: ')
        if respuesta.lower() == 's':
            arbol = arbol.izq
        elif respuesta.lower() == 'n':
            arbol = arbol.der
        else:
            print('Respuesta inválida. Por favor vuelva a intentarlo.')
            print('Presione "Enter" para continuar')
            input()
            print('\n'*60)
    print("\nADIOS!")

consultar(arbol)


