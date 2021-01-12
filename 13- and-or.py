print("Programa de becas año 2020")
distancia_escuela=int(input("Introduce la distancia a la escuela en kilometros: "))
print(distancia_escuela)

numero_hermanos=int(input("Introduce el numero de hermanos en el centro: "))
print(numero_hermanos)

salario_familiar=int(input("Introduce salario anual bruto: "))
print(salario_familiar)

if distancia_escuela>40 and numero_hermanos>2 or salario_familiar<=20000:
	print("Tienes derecho a beca")
else:
	print("No tiene derecho a beca")

#El "and" seria un "y si ademas"
#El "or" es un "o si no"