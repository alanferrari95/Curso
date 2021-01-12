class empleado:
	def __init__(self, nombre, cargo, salario):
		self.nombre=nombre
		self.cargo=cargo
		self.salario=salario

	def __str__(self):
		return "{}, que trabaja como {}, tiene un salario de ${}".format(self.nombre, self.cargo, self.salario)


listaempleados=[

empleado("Juan","Director", 7500),
empleado("Ana","Presidente", 9350),
empleado("Florencia","Administrativo", 2350),
empleado("Leilen","Secretaria", 1800),
empleado("Alan","Jugador", 6632)

]

def calculo_comision(empleado):
	if empleado.salario<=3000:

		empleado.salario=empleado.salario*1.03

	return empleado

listaempleadoscomision=map(calculo_comision, listaempleados)

for i in listaempleadoscomision:
	print(i)