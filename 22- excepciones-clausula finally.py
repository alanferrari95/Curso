def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

#como no se puede dividir por cero, se crea codigo de excepcion
def divide(num1,num2):	
	try:	
		return num1/num2
	except ZeroDivisionError:
		print("No se puede dividir entre 0")
		return "Operacion erronea"
	
#Si introducimos texto tambien nos da error, para evitarlo hacemos:
while True:
	try:
		op1=(int(input("Introduce el primer número: ")))

		op2=(int(input("Introduce el segundo número: ")))	
		break	
	except ValueError:
		print("Los valores introducidos no son correctos. Intentalo nuevamente")

"""
Al hacer un "while true" estamos diciendo que es un bucle infinito, en este caso se podria leer de la siguiente forma:
Try: Intenta poner un valor en op1 y un valor en op2; si no hubo ningun error, salimos del bucle con el "break". 
Si los datos que ingresamos generan el error "ValueError", lo que nos dice el programa es lo siguiente: 
Aparece el error ValueError, quiere decir que los valores introducidos son incorrectos, asi que te llevo otra vez 
al try para que lo intentes nuevamente. 
Entonces se forma un bucle infinito entre: intentalo, si lo pusiste bien genial, sino, volve a intentarlo
"""
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(op1,op2))

elif operacion=="resta":
	print(resta(op1,op2))

elif operacion=="multiplica":
	print(multiplica(op1,op2))

elif operacion=="divide":
	print(divide(op1,op2))

else:
	print ("Operación no contemplada")


print("Operación ejecutada. Continuación de ejecúción del programa ")