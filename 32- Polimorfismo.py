#Un objeto puede cambiar de forma dependiendo el contexto donde se utilice y por lo tanto tambien su comportamiento
#Ejemplo: pasa de ser un camion a ser un coche.

class coche():
	def desplazamiento(self):
		print("Me desplazo utilizando cuatro ruedas")

class moto():
	def desplazamiento(self):
		print("Me desplazo utilizando dos ruedas")

class camion():
	def desplazamiento(self):
		print("Me desplazo utilizando seis ruedas")

def desplazamientovehiculo(vehiculo):
	vehiculo.desplazamiento()

mivehiculo=moto()
desplazamientovehiculo(mivehiculo) 
