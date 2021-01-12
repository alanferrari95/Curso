def devuelve_ciudades(*ciudades): #detalle en la descripcion
	for elemento in ciudades:
		yield from elemento


ciudades_devueltas=devuelve_ciudades("Madrid", "Barcelona", "Bilbao", "Valencia")

print(next(ciudades_devueltas))

print(next(ciudades_devueltas))


"""
La diferencia entre un yield y un yield from es que el yield devuelve un elemento y el yield from devuelve como está compuesto el elemento.
Usando este caso como ejemplo, si yo utilizaría solamente el yield, me devuelve Madrid, Barcelona, etc, etc.
Como utilizo el yield from y su finalidad es mostrarme como esta compuesto el elemento, me van apareciendo 1 a 1 la composicion. M, a, d, r, i, d....

*ciudades: En python cuando ponemos un * antes de un argumento le estamos indicando que va a recibir un numero indeterminado de elementos y que los 
va a recibir en forma de tupla
"""

