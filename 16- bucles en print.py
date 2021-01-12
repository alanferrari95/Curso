#desde el 5 hasta el 30 contando de 5 en 5
for i in range(5,31,5):
	print(f"valor de la variable {i}") #la f une el texto con el valor de la variable

print("---------")

#desde el 5 hasta el 9
for i in range(5,10):
	print(f"valor de la variable {i}")

print("---------")

valido=False
email=input("introduce tu email: ")

for i in range(len(email)):
	if email[i]=="@":
		valido=True

if valido:
	print("El email es correcto")

else:
	print("Email incorrecto")