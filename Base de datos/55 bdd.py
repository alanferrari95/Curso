import sqlite3

miconexion=sqlite3.connect("PrimeraBase")

micursor=miconexion.cursor()

#Creamos una tabla
#micursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULOS VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

#le agregamos articulos
#micursor.execute("INSERT INTO PRODUCTOS VALUES('BALON', 15, 'DEPORTES')")

#creamos una lista
#variosproductos=[

	#("Camiseta",10,"Deportes"),
	#("Jarron",90,"Ceramica"),
	#("Camion",10,"Jugueteria")


#]

#con esta sentencia ingresa en PRODUCTOS la lista recien creada. Los ? son por cada
#parametro que tiene la lista.
#micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)", variosproductos)

micursor.execute("SELECT * FROM PRODUCTOS")

#devuelve los registros
variosproductos=micursor.fetchall()
#ver productos como lista
#print(variosproductos)

#ver productos en bucle for
for i in variosproductos:
	print("Nombre articulo: ",i[0], "Seccion: ",i[2])

miconexion.commit()


miconexion.close()