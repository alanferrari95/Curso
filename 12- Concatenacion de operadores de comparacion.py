salario_presidente=int(input("Intrudice salario presidente: "))
print("Salario presidente: " + str(salario_presidente))

salario_director=int(input("Intrudice salario director: "))
print("Salario director: " + str(salario_director))

salario_jefe_area=int(input("Intrudice salario jefe de area: "))
print("Salario jefe de area: " + str(salario_jefe_area))

salario_administrativo=int(input("Intrudice salario administrativo: "))
print("Salario administrativo: " + str(salario_administrativo))

#concatenacion de operadores de comparacion

if salario_administrativo<salario_jefe_area<salario_director<salario_presidente:
	print("Todo funciona correctamente")
else:
	print("Algo falla en esta empresa")

