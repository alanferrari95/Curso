#Tupla
mitupla1=("celular", "lapiz", "billetera", 2, 6, 12, 2, 2)

#Convertir Tupla en lista
milista1=list(mitupla1)

#Diferencio la tupla de la lista por los corchetes y parentesis
print(milista1)
print(mitupla1)

#convertir lista en tupla
milista2=[1, 3, "alan"]
mitupla2=tuple(milista2)
print(mitupla2)

#Comprobar dato en lista
print("alan" in milista2)

#contar cuantos elementos se encuentran en una tupla
print(mitupla1.count(2))

#Longitud de una tupla
print(len(mitupla1))

#Tupla sin parentesis. Esto es un empaquetado de tupla
mitupla3="fibron", "amarillo", 3
print(mitupla3)

#Desempaquetado de tupla. 
mitupla3=("veinte", "pesos", 27, "enero")
cantidad, moneda, dia, fecha=mitupla3
print(cantidad)
print(moneda)
print(dia)
print(fecha)