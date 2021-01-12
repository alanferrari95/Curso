edad=int(input("introduce la edad: "))

while edad<0 or edad>100:
	print("Introdujiste una edad incorrecta")
	edad=int(input("introduce la edad: "))

print("Gracias por colaborar. Puedes pasar")
print("edad del usuario " + str(edad))
