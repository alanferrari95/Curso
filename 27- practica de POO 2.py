#mi clase tiene 5 propiedades
class coche():
	#esto es un constructor. Se utiliza para mencionar el estado inicial a los objetos que pertenecen a la clase
	def __init__(self):
		#cuando agregamos __ estamos encapsulandolo, es decir, que no se pueda modificar desde afuera
		self.__largochasis=250
		self.__anchochasis=120
		self.__ruedas=4
		self.__enmarcha=False
#esta clase tiene 2 compartamientos. Uno arranca y la otra nos dice los detalles del auto.
	def arrancar(self,arrancamos):
		self.__enmarcha=arrancamos
		if(self.__enmarcha):
			return "El coche esta en marcha"
		else:
			return "El coche está parado"
		

	def estado(self):
		print("El coche  tiene ",self.__ruedas, "ruedas. Un ancho de ",self.__anchochasis, "y un largo de ",
			self.__largochasis)
		
#instanciar/ejemplerizar una clase
micoche=coche()

print(micoche.arrancar(True))

micoche.estado()

print("-------------A continuacion creamos el segundo objeto-------------")

micoche2=coche()

print(micoche2.arrancar(False))

micoche2.__ruedas=2 

micoche2.estado()

