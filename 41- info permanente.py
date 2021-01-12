import pickle

class Persona():
	def __init__(self, nombre, genero, edad):
		self.nombre=nombre
		self.genero=genero
		self.edad=edad
		print("Se ha creado una persona nueva con el nombre de ",self.nombre)

	def __str__(self):
		return "{} {} {}".format(self.nombre, self.genero, self.edad)

class listapersonas():
	personas=[]

	def __init__(self):
		listadepersonas=open("ficheroexterno", "ab+")
		listadepersonas.seek(0)
		try:
			self.personas=pickle.load(listadepersonas)
			print("Se cargaron {} personas del fichero externo".format(len(self.personas)))
		except:
			print("El fichero está vacio")
		finally:
			listadepersonas.close()
			del (listadepersonas)

	def agregarpersonas(self, p):
		self.personas.append(p)
		self.guardarpersonasenficheroexterno()

	def mostrarpersonas(self):
		for p in self.personas:
			print(p)

	def guardarpersonasenficheroexterno(self):
		listadepersonas=open("ficheroexterno", "wb")
		pickle.dump(self.personas, listadepersonas)
		listadepersonas.close()
		del (listadepersonas)

	def mostrarinfoficheroexterno(self):
		print("La informacion del fichero externo es la siguiente:")
		for p in self.personas:
			print (p)

milista=listapersonas()
persona=Persona("ana", "femenino", 19)
milista.agregarpersonas(persona)
milista.mostrarinfoficheroexterno()


