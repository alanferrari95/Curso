#documentar programas. Incluir comentarios en clases, metodos, modulos, etc.
class areas:
	"""documentacion del area, son funciones"""
	def areacuadrado(lado):
		"""esta funcion sirve para calcular el area de un cuadrado.
		Esto se llama documentacion"""
		return "el area del cuadrado es: " + str(lado*lado)

	def areatriangulo(base, altura):
		"""calcula el area de un triangulo utilizando base y altura"""
		return "el area del triangulo es: " + str((base*altura)/2)


'''print(areas.areacuadrado(5))
#imprime la documentacion que es lo que esta entre """comillas"""
print(areas.areacuadrado.__doc__)

#otra forma es con help
help(areas.areacuadrado)

#Las funciones de este tipo SIEMPRE va identada
help(areas.areatriangulo)'''

help(areas)


