class Personaje:
    def __init__(self, nombre, heroe=True):
        self.__nombre = nombre.upper()
        self.heroe = heroe

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre.upper()

    def __gt__(self, other):
        return self.nombre > other.nombre

    def __eq__(self, other):
        return self.nombre == other.nombre

    def __lt__(self, other):
        return self.nombre < other.nombre

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return '<{nombre}, {heroe}>'.format(nombre=self.nombre, heroe=self.heroe)

    def es_heroe(self):
        return self.heroe

    def es_villano(self):
        return not self.heroe

personajes = []

personajes.append(Personaje('SPIDERMAN'))
personajes.append(Personaje('CAPITAN AMERICA'))
personajes.append(Personaje('IRONMAN'))
personajes.append(Personaje('DEADPOOL'))
personajes.append(Personaje('THOR'))
personajes.append(Personaje('HULK'))
personajes.append(Personaje('DOCTOR STRAGE'))
personajes.append(Personaje('MAGNETO', False))
personajes.append(Personaje('VENOM', False))
personajes.append(Personaje('APOCALIPSIS', False))
personajes.append(Personaje('GALACTUS', False))
personajes.append(Personaje('THANOS', False))
personajes.append(Personaje('KINGPIN', False))
