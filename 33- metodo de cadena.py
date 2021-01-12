nombreusuario=input("Introduce tu nombre de usuario: ")

#como aplicar metodo al string= funcion.metodo
#todo en mayusculas
print("Tu nombre es: ",nombreusuario.upper())


edad=input("Introduce la edad: ")

while edad.isdigit()==False:
	print("Por favor introduce un valor numerico")
	edad=input("Introduce la edad: ")

if (int(edad)<18):
	print("no puede pasar")
else:
	print("no puede pasar")

