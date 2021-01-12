#mi clase tiene 5 propiedades
class coche():
	largochasis=250
	anchochasis=120
	ruedas=4
	enmarcha=False
#esta clase tiene 2 compartamientos. Uno arranca y la otra nos dice el estado del auto.
	def arrancar(self):
		self.enmarcha=True

	def estado(self):
		if(self.enmarcha):
			return "El coche está en marcha"
		else:
			return "El coche está parado"

#instanciar/ejemplerizar una clase
micoche=coche()

print("el largo del chasis es de",micoche.largochasis, "centimetros")
print("el coche tiene",micoche.ruedas, "ruedas")
micoche.arrancar()

print(micoche.estado())
