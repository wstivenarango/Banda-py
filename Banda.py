  
from random import randint, uniform,random


class Instrumento:
    def tocar(self):
        return("Tocando")
    def preparar(self):
        return("Afinando")


class Guitarra(Instrumento):
    nombre = 'Guitarra'
    def __init__(self):
        self = self


class Bajo(Instrumento):
    nombre = 'Bajo'
    def __init__(self):
        self = self        


class Violin(Instrumento):
    nombre = 'Violin'
    def __init__(self):
        self = self


class Arpa (Instrumento):
    nombre = 'Arpa'
    def __init__(self):
        self = self


class Viola (Instrumento):
    nombre = 'Viola'
    def __init__(self):
        self = self


class Ukelele (Instrumento):
    nombre = 'Ukelele'
    def __init__(self):
        self = self

class Violin_Chelo (Instrumento):
    nombre = 'Violin Chelo'
    def __init__(self):
        self = self        

class Contrabajo (Instrumento):
    nombre = 'Contrabajo'
    def __init__(self):
        self = self   


class Banda():
    def crearBanda(self,numeromusicos):
        instrumentos = [Guitarra(),Bajo(),Violin(),Arpa(),Viola(),Ukelele(), Violin_Chelo(),Contrabajo()]
        banda = []
        for i in range(0,numeromusicos):
            ins = randint(0,7)
            obj =instrumentos[ins]
            banda.append(obj)
        j = 1
        for i in banda:
          
            j = j+1
        return banda
    def afinarBanda(self, banda, numeromusicos ):
        j = 1
        for i in banda:
            print(i.preparar(),i.nombre)
            j = j+1
    def tocarBanda(self, banda, numeromusiscos):
        j = 1
        for i in banda:
            print(i.tocar(),i.nombre)
            j = j+1
banda = Banda()
b = []
numeromusicos = randint(5,10)
print("La banda esta conformada por", numeromusicos, " musicos")
b = banda.crearBanda(numeromusicos)
print(" ")
banda.afinarBanda(b,numeromusicos)
print(" ")
banda.tocarBanda(b,numeromusicos)
print(" ")
print("Disfruta la banda parranda")
