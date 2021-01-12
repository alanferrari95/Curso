import pickle


class vehiculos():
	def __init__(self, marca, modelo):
		self.marca=marca
		self.modelo=modelo
		self.enmarcha=False
		self.acelera=False
		self.frena=False

	def arrancar(self):
		self.enmarcha=True

	def acelerar(self):
		self.acelera=True

	def frenar():
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca, "\nModelo: ", self.modelo, "\nEn marcha: ",self.enmarcha, "\nAcelerando: ",self.acelera, "\nFrenando: ",self.frena)


coche1=vehiculos("mazda","mx5")		
coche2=vehiculos("seat","leon")		
coche3=vehiculos("renault","megane")		

coches=[coche1, coche2, coche3]
fichero=open("loscoches", "wb")

pickle.dump(coches, fichero)

fichero.close()

del (fichero)

ficheroaperutra=open("loscoches","rb")

miscoches=pickle.load(ficheroaperutra)

ficheroaperutra.close()

for c in miscoches:
	print(c.estado())