#creamos una lista. Las listas llevan paréntesis
milista=["cepillo", "billetera", 2, 5]
print(milista)

#mostramos un elemento de la lista. Los elementos arrancan desde el 0, 1, 2....
print(milista[1])

#indice negativo, arranca de derecha a izqueirda. Arranca a contar desde 1, 2,...
print(milista[-2])

#mostrar parte de una lista. Primer termino "desde" y excluye el segundo termino
print(milista[0:3])

#agrega un elemento al final de la lista
milista.append("juan")

#agrega elemento en una posicion. Primero la posición y depsues el valor
milista.insert(2,125)
print(milista)

#agregar varios elementos a la lista. Los elementos van entre []
milista.extend(["franco", 324, "pañuelo"])
print(milista)

#otro elemento al final. El "final" de la lista es por orden.
milista.append("alan")
print(milista)

#Buscar elemento en la lista. "True" si se encuenta y "false" si no se encuentra
print("pepe" in milista)
print("alan" in milista)

#eliminar elementos
milista.remove("franco")
print(milista)

#eliminar el ultimo elemento agregado
milista.pop()
print(milista)

#Sumar listas
milista2=["futbol", "tenis", "rugby"]
print(milista2)
milista3=milista+milista2
print(milista3)