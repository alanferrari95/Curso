def generapares2(limite2):
	num2=1
	milista=[]
	while num2<limite2:
		milista.append(num2*2)
		num2+=1
	return milista

print(generapares2(10))


#ejercicio 2
def generapares(limite):
	num=1
	while num<limite:
		yield num*2 #yield construye como una lista, es un objeto iterable y va mostrando de 1 en 1 a medida que se lo solicita
		num+=1
devuelvepares=generapares(10)

print(next(devuelvepares)) #la funcion "next" hace que nos devuelva el primer (o sigueinte) valor almacenado en el yield 
print("aqui prodria ir mas codigo..")

print(next(devuelvepares))
print("aqui prodria ir mas codigo..")

print(next(devuelvepares))
print("aqui prodria ir mas codigo..")
