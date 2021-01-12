class persona():
	def __init__(self, nombre, edad, lugar_residencia):
		self.nombre=nombre
		self.edad=edad
		self.lugar_residencia=lugar_residencia

	def descripcion(self):
		print("Nombre: ",self.nombre, "edad: ",self.edad, "residencia: ",self.lugar_residencia)

class empleado(persona):
	def __init__(self, salario, antiguedad, nombre_empleado, edad_empleado, residencia_empleado):
		super().__init__(nombre_empleado, edad_empleado, residencia_empleado) #llama al metodo de la clase padre
		self.salario=salario
		self.antiguedad=antiguedad

	def descripcion(self):
		super().descripcion() #llama al metodo de la clase padre. Nos "ahorramos" volver a escribir todo
		print("salario: ",self.salario, "antiguedad: ",self.antiguedad)

manuel=empleado(1500, 15, "Manuel", 55, "colombia")
manuel.descripcion()

#Principio de sustitucion: "es siempre un/a". Si un objeto pertenece a la super clase o a una clase.
print(isinstance(manuel, persona)) #nos informa si un objeto es instancia de una clase determinada


