def funcion_decoradora(funcion_parametro):

	def funcion_interior():
		#acciones adicionales que decoran
		print("Vamos a realizar un cálculo")
		funcion_parametro()
		#acciones adicionales que decoran
		print("Hemos realizado el cálculo")

	return funcion_interior

@funcion_decoradora
def suma():
	print(15+20)
@funcion_decoradora
def resta():
	print(30-10)

suma()

resta()