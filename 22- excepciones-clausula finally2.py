def divide():
	while True:
		try:
			op1=(float(input("Introduce el primer numero: ")))
			op2=(float(input("Introduce el segundo numero: ")))
			print("La division es: " + str(op1/op2))
			break
		except ValueError:
			print("El valor introducido es erroneo")	
		except ZeroDivisionError:
			print("No se puede dividir entre cero")

	print("Calculo finalizado con éxito.")

divide()