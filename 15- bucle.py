#esto es basico pero hay que arreglarlo
contar_ar=0
contar_pu=0
mi_email=input("Escribe tu email: ")

for i in mi_email:
	if i=="@":
		contar_ar=contar_ar+1
	if i==".":
		contar_pu=contar_pu+1

if contar_ar==1 and contar_pu>=1:
	print("El email es correcto")
else:
	print("El email no es correcto")

for i in range(5): #rango de 5
	print("hola")
