#importar modulo, una opcion es desde el "import"
#import modulos

#modulos.sumar(4, 10)
#modulos.restar(10, 4)

#y esta es otra forma, salvo que solo trae el metodo "sumar"
from modulos import sumar
sumar(4, 5)

#si queremos que traiga TODAS las funciones, hay que poner un *
from modulos import *
sumar(3,3)
restar(10,7)
multiplicar(4,4)