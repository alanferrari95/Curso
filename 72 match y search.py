import re

#"match" busca al comienzo del texto y 
#"search" busca en toda la cadena del texto

nombre1="Jara López"
nombre2="Antonio Gómez"
nombre3="Lara López"


#Distingue entre mayusculas y minusculas. 
#El patron ignorecase ignora entre mayusculas y minusculas
'''if re.match("Sandra", nombre1, re.IGNORECASE):
	print("Hemos encontrado el nombre")

else:
	print("No lo hemos encontrado")


#busca palabras que inicien con cualquier letra y sigan con "ara"
if re.match(".ara", nombre1):
	print("Hemos encontrado el nombre")

else:
	print("No lo hemos encontrado")

cadena1="Jara López"
cadena2="56525584"
cadena3="a546465"

if re.match("\d", cadena2):
	print("Hemos encontrado el nombre")

else:
	print("No lo hemos encontrado")

if re.search("López", nombre1):
	print("Hemos encontrado el nombre")

else:
	print("No lo hemos encontrado")'''

codigo1="dslajsd71kasdnklj"
codigo2="alsdklasdk alsdkla"
codigo3="kawdlknadlndlnwalnkwdawd71"

if re.search("71", codigo1):
	print("Hemos encontrado el nombre")

else:
	print("No lo hemos encontrado")

