#Comprobamos si funciona o no nuestras funciones

def areatriangulo(base,altura):
	"""
	Calcula el area de un triangulo dado.
	>>> areatriangulo(3,6)
	'El área del triangulo es: 9.0'

	>>> areatriangulo(4,5)
	'El área del triangulo es: 10.0'

	>>> areatriangulo(9,3)
	'El área del triangulo es: 13.5'

	"""
	return "El área del triangulo es: " +str((base*altura)/2)


def compruebaemail(emailusuario):
	"""
	la funcion compruebaemail evalua un email recibido en busca de la @.
	Si tiene una @ es correcto, si tiene mas de una @ es incorrecto, si la
	@ está al final es incorrecto

	>>> compruebaemail("juan@cursos.es")
	True
	>>> compruebaemail("juan@cursos.es@") 
	False
	>>> compruebaemail("juancursos.es@")
	False
	>>> compruebaemail("juancursos.es")
	False

	"""
	arroba=emailusuario.count("@")

	if arroba!=1 or emailusuario.rfind("@")==(len(emailusuario)-1) or emailusuario.find("@")==0:
		return False
	else:
		return True

import doctest
doctest.testmod()