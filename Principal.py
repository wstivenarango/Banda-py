from Banda import *

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

