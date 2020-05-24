from abc import ABC, abstractmethod

class Instrumento(ABC):
    @abstractmethod
    def tocar(self):
       pass
    @abstractmethod
    def preparar(self):
       pass


class Guitarra(Instrumento):
    nombre = 'Guitarra'

    def tocar(self):
        return("tocando Guitarra")
    def preparar(self):
        return ("afinando Guitarra")
    def __init__(self):
        self = self
   


class Bajo(Instrumento):
    nombre = 'Bajo'    
    def tocar(self):
        return("tocando Bajo")
    def preparar(self):
        return ("afinando Bajo")
      


class Violin(Instrumento):
    nombre = 'Violin'  
    def tocar(self):
        return("tocando Violin")
    def preparar(self):
        return ("afinando Violin")
    
    def __init__(self):
        self = self


class Arpa (Instrumento):
    nombre = 'Arpa'  
    def tocar(self):
        return("tocando Arpa")
    def preparar(self):
        return ("afinando Arpa")
    
    def __init__(self):
        self = self


class Viola (Instrumento):
    nombre = 'Viola' 
    def tocar(self):
        return("tocando Viola")
    def preparar(self):
        return ("afinando Viola ")
   
    def __init__(self):
        self = self


class Ukelele (Instrumento):
    nombre = 'Ukelele' 
    def tocar(self):
        return("tocando Ukelele")
    def preparar(self):
        return ("afinando Ukelele")
   
    def __init__(self):
        self = self

class Violin_Chelo (Instrumento):
    nombre = 'Violin Chelo'
    def tocar(self):
        return("tocando Chelo")
    def preparar(self):
        return ("afinando Chelo")
   
    def __init__(self):
        self = self        

class Contrabajo (Instrumento):
    nombre = 'Contrabajo'
    def tocar(self):
        return("tocando Contrabajo")
    def preparar(self):
        return ("afinando Contrabajo")
   
    def __init__(self):
        self = self 
