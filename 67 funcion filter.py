'''def numero_pars(num):
	if num % 2==0:
		return True

numero=[17,27,48,41,25,23,36,68,61]

print(list(filter(lambda numero_pars: numero_pars%2==0, numero)))'''

class empleados:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{}, que trabaja como {}, tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)


listaempleados=[

empleados("Juan","Director", 75000),
empleados("Ana","Presidente", 180000),
empleados("Florencia","Administrativo", 23500),
empleados("Leilen","Secretaria", 18000),
empleados("Alan","Jugador", 66352)

]

salario_altos=filter(lambda empleado:empleado.salario>50000, listaempleados)

for i in salario_altos:
	print(i)