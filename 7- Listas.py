#listas: nombrelista=[elemento1,elemento2,element3]
#se le puede agregar elementos
#El indice de las listas empiezan de 0, 1, 2, 3....

milista=["juan","alan","zulema"]

print(milista[:]) #imprime todos los elementos
print(milista[0]) #imprime solo el primer elemento
print(milista[1:3]) #imprime el 1 y el 2
print(milista[-1]) #imprime el ultimo

milista.append("bruno") #agrega "bruno" al final de la lista

print(milista) 

milista.insert(2,"leilen") #agrega a "leilen" en la posicion numreo 2
print(milista)

milista.extend(["clara","sofia","maite"]) #agrega varios elementos al final de la lista
print(milista)

print(milista.index("clara")) #en que posicion está un elemento

print("clara" in milista) #imprime true/false si el elemento se encuentra en la lista

milista.remove("maite") #eliminar un elemento
print(milista)

milista.pop() #elimina el ultimo elemento de la isla
print(milista)

milista2=[1,2,3]
print(milista2)

milista3=milista2+milista #unir listas
print(milista3)

print(milista2 * 2) #imprime 2 veces la lista 2


print("holaaaa")