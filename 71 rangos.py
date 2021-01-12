import re

lista_nombre=["Ana",
				"pedro",
				"maria",
				"rosa",
				"sandra"
				"celia"]


#devuelve rango entre la o y la t
for i in lista_nombre:
	if re.findall("[o-t]", i):

		print(i)

#devuelve rango entre la O y la T
for i in lista_nombre:
	if re.findall("[O-T]", i):

		print(i)


lista_nombre=["Ma.1",
				"Se1",
				"Ma2",
				"Ba1",
				"Ma:3",
				"Va1",
				"Va2",
				"Ma4",
				"MaA",
				"Ma.5",
				"MaB",
				"Ma:C"]

for i in lista_nombre:
	if re.findall("Ma[.:]", i):

		print(i)
