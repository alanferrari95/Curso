#mi clase tiene 5 propiedades
class coche():
	#esto es un constructor. Se utiliza para mencionar el estado inicial
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
			chequeo=self.__chequeo_interno()
		
		if(self.__enmarcha and chequeo):
			return "El coche esta en marcha"
		
		elif(self.__enmarcha and chequeo==False):
			return "Algo ha ido mal en el chequeo"
		
		else:
			return "El coche está parado"
		

	def estado(self):
		print("El coche  tiene ",self.__ruedas, "ruedas. Un ancho de ",self.__anchochasis, "y un largo de ",
			self.__largochasis)

	def __chequeo_interno(self): #encapsula el metodo, solo se puede acceder desde afuera. Funciona solo desde dentro de la clase.
		print("Realizando chequeo interno")
		self.gasolina="ok"
		self.aceite="ok"
		self.puertas="cerradas"

		if(self.gasolina=="ok" and self.aceite=="ok" and self.puertas=="cerradas"):
			return True
		else:
			return False
		
#instanciar/ejemplerizar una clase
micoche=coche()

print(micoche.arrancar(True))

micoche.estado()

print("-------------A continuacion creamos el segundo objeto-------------")

micoche2=coche()

print(micoche2.arrancar(False))

micoche2.estado()

