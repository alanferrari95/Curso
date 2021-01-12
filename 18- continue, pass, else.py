#instruccion continue. Si detecta una letra H, continua el bucle desde el inicio. En este caso, no printea la letra.
for letra in "python":
	if letra=="h":
		continue

	print("letra: " + letra)


nombre="pildoras informaticas"
contador=0
for i in nombre:
	if i==" ":
		continue
	contador+=1
	
print("cantidad de letras: " + str(contador))

#cuando encuentra un @ sale del bucle
email=input("introduce tu email: ")

for i in email:
	if i=="@":
		arroba=True
		break;

else:
	arroba=False

print(arroba)