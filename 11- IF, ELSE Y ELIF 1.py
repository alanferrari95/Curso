print("verificacion de acceso")

edad_usuario=int(input("Introduce tu edad, por favor: "))

if edad_usuario<18:
	print("no puede pasar")
elif edad_usuario>100:
	print("edad incorrecta")
else:
	print("puede pasar")
print("el programa ha finalizado")

#el "elif" se pone como un condicional extra, sino el "else" va a acompañar al "if" mas cercano


