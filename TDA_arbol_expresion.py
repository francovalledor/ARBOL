from TDA_arbol import ArbolBinario

class Operadores:
    SUMA = '+'
    RESTA = '-'
    MULTIPLICACION = '*'
    DIVISION = '/'

class ArbolExpresion(ArbolBinario):
    def __init__(self, expresion):
        """
        Carga una expresión algebraica
        Operadores permitidos: +-*/()
        Valores decimales no están permitidos
        Ejemplo: 5*(2+8)-2/4
        """
        super().__init__()
        self.original = expresion
        self.expresion = expresion
        
        self.__limpiar()
        if not self.__es_valida():
            raise Exception('Expresion inválida: {expresion}'.format(expresion=self.expresion))

        self.__parser()

    def resolver(self):
        if self.es_hoja():
             return int(self.valor)
        else:
            izq = self.izq.resolver()
            der = self.der.resolver()

            if self.valor == '+':
                return izq + der
            elif self.valor == '-':
                return izq - der
            elif self.valor == '*':
                return izq * der
            else:
                if der == 0:
                    raise Exception('Error, division por cero')
                
                return izq / der

    def __limpiar(self):
        """Elimina los parentesis sobrantes al inicio y al final"""
        aux_expresion = self.expresion
        while (aux_expresion[0] == '(') and (aux_expresion[-1] == ')'):
            aux_expresion = aux_expresion[1:-1]
        
        if not self.__hay_nivel_negativo(aux_expresion):
            self.expresion = aux_expresion

    def __parser(self):
        if not self.__hay_operadores():
            self.valor = self.expresion
            return
        
        if self.__hay_operadores_SR():
            parte_izq = ''
            parte_der = self.expresion
            siguiente = ''
            nivel = 0

            #inicio
            while len(parte_der) > 1:
                parte_izq += siguiente
                siguiente = parte_der[0]
                parte_der = parte_der[1:]
                if self.__es_parentesis_abierto(siguiente):
                    nivel += 1
                elif self.__es_parentesis_cerrado(siguiente):
                    nivel -= 1
                if self.__es_SR(siguiente) and nivel == 0:
                    self.valor = siguiente
                    self.izq = ArbolExpresion(parte_izq)
                    self.der = ArbolExpresion(parte_der)
                    return
        
        if self.__hay_operadores_MD():
            parte_izq = ''
            parte_der = self.expresion
            siguiente = ''
            nivel = 0

            #inicio
            while len(parte_der) > 1:
                parte_izq += siguiente
                siguiente = parte_der[0]
                parte_der = parte_der[1:]
                if self.__es_parentesis_abierto(siguiente):
                    nivel += 1
                elif self.__es_parentesis_cerrado(siguiente):
                    nivel -= 1
                if self.__es_MD(siguiente) and nivel == 0:
                    self.valor = siguiente
                    self.izq = ArbolExpresion(parte_izq)
                    self.der = ArbolExpresion(parte_der)
                    return

    def __es_numero(self, char):
        """Char es numero?"""
        return char in '0123456789'
    
    def __es_SR(self, char):
        """Char es '+' o '-' ? """
        return char in '+-'

    def __es_MD(self, char):
        """Char es '*' o '/' ? """
        return char in '*/'

    def __es_operador(self, char):
        """Char es + - * o / ? """
        return char in '+-*/'


    def __es_parentesis(self, char):
        return char in '()'
    
    def __es_parentesis_abierto(self, char):
        return char == '('
    
    def __es_parentesis_cerrado(self, char):
        return char == ')'

    def __hay_parentesis(self, string=None):
        if not string:
            string = self.expresion
            
        if ('(' in string) and (')' in string):
           if string.index('(') < string.index(')'):
               return True
        return False

    def __hay_operadores_SR(self, string=None):
        """ Hay operadores de suma o de resta """
        if not string:
            string = self.expresion
        hay_suma = '+' in string
        hay_resta = '-' in string
        return hay_resta or hay_suma

    def __hay_operadores_MD(self, string=None):
        """ Hay operadores de multiplicacion o division """
        if not string:
            string = self.expresion

        hay_multiplicacion = '*' in string
        hay_division = '/' in string
        return hay_division or hay_multiplicacion
    
    def __hay_operadores(self, string=None):
        """ Hay operadores + - * / """
        if not string:
            string = self.expresion
        return self.__hay_operadores_SR(string) or self.__hay_operadores_MD(string)

    def __es_valida(self):
        """Es una expresion valida?"""
        #Si el primer o el ultimo elemento es un operador es inválida
        primer = self.expresion[0]
        ultimo = self.expresion[-1]

        if self.__es_operador(primer) or self.__es_operador(ultimo):
            return False

        #Si la cantidad de "(" difiere de la cantidad de ")" es inválida
        if self.expresion.count('(') != self.expresion.count(')'):
            return False

        parte_izq = ''
        actual = ''
        nivel = 0
        parte_der = self.expresion
        if self.__hay_parentesis():
            while len(parte_der)>1:
                parte_izq += actual
                actual = parte_der[0]
                siguiente = parte_der[1]
                parte_der = parte_der[1:]
                if self.__es_parentesis_abierto(actual):
                    nivel += 1
                elif self.__es_parentesis_cerrado(actual):
                    nivel -= 1

                #Si el nivel de parentesis es un valor negativo, es inválida
                if nivel < 0:
                    return False
                #Si hay 2 operadores seguidos es inválida
                if self.__es_operador(actual) and self.__es_operador(siguiente):
                    return False
                #Si hay '(' y no está precedido por un operador es inválida
                if self.__es_parentesis_abierto(siguiente) and not self.__es_operador(actual):
                    return False
                #Si hay ')' y no está seguido de un operador es inválida
                if self.__es_parentesis_cerrado(actual) and not self.__es_operador(siguiente):
                    return False
                #Si hay parentesis vacios es inválida
                if self.__es_parentesis_abierto(actual) and self.__es_parentesis_cerrado(siguiente):
                    return False

        #Si no, es válida
        return True

    def __hay_nivel_negativo(self, expresion=None):
        if not expresion:
            expresion = self.expresion

        nivel = 0
        for char in expresion:
            if self.__es_parentesis_abierto(char):
                nivel += 1
            elif self.__es_parentesis_cerrado(char):
                nivel -= 1
            if nivel < 0:
                return True

        return False


    def __repr__(self):
        izq = self.izq if self.izq else ''
        der = self.der if self.der else ''
        if not izq and not der:
            return self.valor
        return '({izq} {self.valor} {der})'.format(izq=izq, der=der, self=self)
