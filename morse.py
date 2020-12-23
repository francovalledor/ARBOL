from TDA_arbol_simple import Arbol

morse = Arbol()

E = morse.izq = Arbol('E') #.
I = E.izq = Arbol('I') #..
S = I.izq = Arbol('S') #...
H = S.izq = Arbol('H') #....
nro5 = H.izq = Arbol('5') #.....

T = morse.der = Arbol('T') #-
M = T.der = Arbol('M') #--
O = M.der = Arbol('O') #---
ninguno = O.der = Arbol() #----
nro9 = ninguno.izq = Arbol('9') #----.


A = E.der = Arbol('A') #.-
W = A.der = Arbol('W') #.--
J = W.der = Arbol('J') #.---
nro1 = J.der = Arbol('1') #.----

R = A.izq = Arbol('R') #.-. 

aux3 = R.der = Arbol() #.-.-
punto = aux3.izq = Arbol('.') #.-.-. Supongo que ese codigo es un punto. Siempre aparece al final.


L = R.izq = Arbol('L') #.-..

N = T.izq = Arbol('N') #-.
D = N.izq = Arbol('D') #-..
B = D.izq = Arbol('B') #-...
nro6 = B.izq = Arbol('6') #-....

K = N.der = Arbol('K') #-.-
C = K.izq = Arbol('C') #-.-.
Y = K.der = Arbol('Y') #-.--

U = I.der = Arbol('U') #..-
F = U.izq = Arbol('F') #..-.

G = M.izq = Arbol('G') #--.

P = W.izq = Arbol('P') #.--.

Q = G.der = Arbol('Q') #--.-
Z = G.izq = Arbol('Z') #--..

V = S.der = Arbol('V') #...-

X = D.der = Arbol('X') #-..-

nro4 = H.der = Arbol('4') #....-
nro3 = V.der = Arbol('3') #...--

nro0 = ninguno.der = Arbol('0') #-----

aux = O.izq = Arbol() #---.
nro8 = aux.izq = Arbol('8') #---..

nro7 = Z.izq = Arbol('7') #--...

aux2 = U.der = Arbol() #..--
nro2 = aux2.der = Arbol('2') #..--


# def mostrar_todos_nodos(arbol):
#     print(arbol.valor)
#     if arbol.der != None:
#         mostrar_todos_nodos(arbol.der)
#     if arbol.izq != None:
#         mostrar_todos_nodos(arbol.izq)

# mostrar_todos_nodos(morse) #Para comprobar visualmente

def descifrar_caracter(codigo, arbol):
    while len(codigo)>0:
        signo = codigo[0]
        codigo = codigo[1:]
        if signo == '.':
            if arbol.izq != None:
               arbol = arbol.izq
            else:
                break
        elif signo == '-':
            if arbol.der != None:
                arbol = arbol.der
            else: 
                break
    return arbol.valor if arbol.valor != None else ''

codigo = '.--. .- ... . / .-.. --- / --.- ..- . / .--. .- ... . / -- .- .- -. .- /.--. .-. --- -- - .- -- . / .- .-.. --. --- / --.- ..- . / ... . --. ..- .. .-. / ... .. . -. -.. --- / ..- ... - . -.. / -. - -- / ..- -. / ... --- .-.. -.. .- -.. --- / .--. . .-. ..-. . -.-. - --- --..-- / ... .. -. --- / ..- -. / -... ..- . -. /.... --- -- -... .-. . .-.-.'
codigo2 = '-. --- ... --- - .-. --- ... / ... --- -- --- ... / .-.. --- ... / -- .- .-.. -.. .. - --- ... / --. ..- .- .-. -.. .. .- -. . ... / -.. . / .-.. .- / --. .- .-.. .- -..- .. .- .-.-.'
codigo3 = '-.-- --- / ... --- .-.. --- / .- -.-. - ..- --- / -.-. --- -- --- / ... ../ . -. / ...- . .-. -.. .- -.. / .-.. --- / ... ..- .--. .. . .-. .- / - --- -.. --- .-.-.'
codigo4 = '-.-. .... .. -.-. --- ... / . ... - --- -.-- / .-.. .-.. . ...- .- -. -.. --- / .-.. .- /..-. .. . ... - .- / .... .- -.-. .. .- / ..- ... - . -.. . ... .-.-.'
codigo5 = '.--. --- -.. .-. .. .- / .... .- -.-. . .-. / . ... - --- / - --- -.. --- / . .-.. /-.. .. .- .-.-.'

def descifrar_mensaje(codigo, arbol):
    mensaje_descifrado = ''
    palabras = codigo.split('/')
    for palabra in palabras:
        descifrada = ''
        letras = palabra.split(' ')
        for letra in letras:
            aux = descifrar_caracter(letra, morse)
            descifrada += aux
        mensaje_descifrado += descifrada + ' '
    print(mensaje_descifrado)

for codigo in (codigo, codigo2, codigo3, codigo4, codigo5):
    descifrar_mensaje(codigo, morse)