import re

lista_nombre=["Ana Gome", 
				"Maria Martin",
				"Sandra Lopez",
				"Santiago Martin",
				"Sandra Fernandez",
				"Mañer Dupon",
				"Niños",
				"Niñas",
				"Camion",
				"camión"]


#devuelve quienes inician con Sandra
for i in lista_nombre:
	if re.findall("^Sandra", i):

		print(i)

#devuelve quienes finalizan con Martin
for i in lista_nombre:
	if re.findall("Martin$", i):

		print(i)

'''#devuelve quienes tienen una ñ
for i in lista_nombre:
	if re.findall("[ñ]", i):

		print(i)'''

#devuelve niños o niñas
for i in lista_nombre:
	if re.findall("Niñ[oa]s", i):

		print(i)

#devuelve con o sin acentos y C c
for i in lista_nombre:
	if re.findall("[Cc]ami[oó]n", i):

		print(i)
