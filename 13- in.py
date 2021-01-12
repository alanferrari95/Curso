print("Asignaturas optativas año 2020")
print("Asignaturas optativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")

opcion=input("Escribe la asignatura escogida: ")
#aca transformo todo lo que esté escrito en la variable "opcion" a minusculas
asignatura=opcion.lower()
#lower() para pasar todo a minusculas y upper() para pasar todo a mayusculas


if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
	print("Asignatura elegida " + asignatura)

else:
	print("La asignatura escogida no esta contemplada")


