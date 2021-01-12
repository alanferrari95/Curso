import math

def raizcuadrada(listanumeros):

	"""
	La funcion devuelve una lista con la raiz cuadrada de los elementos numericos pasado por 
	paramentros en otra lista
	#Esto agrega elementos a la lista desde una lista
	>>> lista=[]
	>>> for i in [4,9,16]:
	...	lista.append(i)
	>>> raizcuadrada(lista)
	[2.0, 3.0, 4.0]

	>>> lista=[]
	>>> for i in [4,-9,16]:
	...	lista.append(i)
	>>> raizcuadrada(lista)
	Traceback (most recent call last):
  		...
	ValueError: math domain error

	"""

	return [math.sqrt(n) for n in listanumeros]


#print(raizcuadrada([9,-16,25,36]))


#probar la documentacion
import doctest
doctest.testmod()

