#Las tuplas son como las listas pero NO SE PUEDEN MODIFICAR, SON INMUTABLES
#Permiten extraer porciones pero el resultado es una nueva tupla
#SI permiten comprobar si un elemento se encuentra en la tupla
#Las tuplas van entre parentesis y no entre corchetes

tupla=(1,2,"juan")
print(tupla[2])

lista=list(tupla) #convertimos la tupla en lista
print(lista)

milista=["flor","garcia","macarena","flor","flor"]
mitupla=tuple(milista) #convertimos la lista en tupla
print(mitupla)
print("flor" in mitupla)

print(mitupla.count("flor")) #contar la cantidad de veces que aparece esa palabra
print(len(mitupla)) #cantidad de elementos en la tupla

mitupla2="franco", 3, 4, "agustin" #empaquetado de tupla
print(mitupla2)

nombre, dia, mes, hermano=mitupla2 #desempaquetado de tupla
print(nombre)
print(dia)

print(mitupla2.index(3)) #buscar en tupla

