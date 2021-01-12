print("programa de evaluacion de notas de alumnos")
#para introducir valor por teclados usamos input()
#TODO DATO INGRESADO A TRAVES DE INPUT() ES CONSIDERADO COMO TEXTO
#la funcion int() transforma en entero cualquier cosa que pongamos en un parametro
nota_alumnos=input("Nota del alumno: ")

#utilizacion del IF
def evaluacion(nota):
	valoracion="aprobado"
	if nota<6:
		valoracion="suspendido"
	return valoracion

print(evaluacion(int(nota_alumnos)))
