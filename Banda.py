from Instrumentos import *  
from random import randint, uniform,random



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
            print(i.preparar())
            j = j+1
    def tocarBanda(self, banda, numeromusiscos):
        j = 1
        for i in banda:
            print(i.tocar())
            j = j+1
