midiccionario={"Alemania":"Berlin","Francia":"Paris","España":"Madrid"}
print(midiccionario["Alemania"])
print(midiccionario)



#Agregar elemento a diccionario y corregirlo
midiccionario["Italia"]="Lisboa"
print(midiccionario)
midiccionario["Italia"]="Roma"
print(midiccionario)



#Eliminar elemento
del midiccionario["España"]
print(midiccionario)


#Diccionario mixto
dicc2={"Argentina":6, 12:"Rey","Pato":"niato"}
print(dicc2)

"""

#Utilziar tupla para asignar clave a valores
mitupla=["España","Francia","Reino Unido","Alemania"]
dicc3={mitupla[0]:"Madrid",mitupla[1]:"Paris",mitupla[2]:"Londres",mitupla[3]:"Berlin"}
print(dicc3)

#acceder a un valor del diccionario
print(dicc2["Argentina"])

#diccionario almacena una tupla de valores
dicc3={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991,1992,1993,1996,1997,1998]}
print(dicc3["anillos"])

#diccionario dentro de diccionario
dicc4={23:"Jordan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1997,1998]}}
print(dicc4)

#Claves que pertenece el diccionario
print(dicc4.keys())
#Valores del diccionario
print(dicc4.values())
#Longitud del diccionario
print(len(dicc4))

"""