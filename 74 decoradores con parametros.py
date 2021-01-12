def funcion_decoradora(funcion_parametro):
	#*args (puedo usar el nombre que quiera). Significa que puede recibir 1 o mas parametros
	#**kwargs para funciones con keywords
	def funcion_interior(*args, **kwargs):
		#acciones adicionales que decoran
		print("Vamos a realizar un cálculo")
		funcion_parametro(*args, **kwargs)
		#acciones adicionales que decoran
		print("Hemos realizado el cálculo")

	return funcion_interior

@funcion_decoradora
def suma(num1,num2, num3):
	print(num1+num2+num3)

	
@funcion_decoradora
def resta(num1,num2):
	print(num1-num2)

def potencia(base, exponente):
	print(base**exponente)

suma(7,5,8)

resta(12,10)

#clave valor
potencia(base=5, exponente=3)

