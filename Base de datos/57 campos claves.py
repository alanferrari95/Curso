import sqlite3

miconexion=sqlite3.connect("GestionProductos")

micursor=miconexion.cursor()

#Creamos la tabla. Los ''' es para cuando tenemos que poner muchas columnas.
#micursor.execute(''':
	#CREATE TABLE PRODUCTOS (
	#CODIGO_ARTICULO VARCHAR(4) PRIMARY KEY,
	#NOMBRE_ARTICULO VARCHAR(50),
	#PRECIO INTEGER,
	#SECCION VARCHAR(20))
#''')

#Comento todo porque sinó se crea 2 veces.

#Creamos la lista [] con tuplas () en su interior.
#productos=[

	#("AR01", "pelota", 20, "juguetería"),
	#("AR02", "pantalón", 15, "confeccion"),
	#("AR03", "destornillador", 25, "ferretería"),
	#("AR04", "jarrón", 45, "cerámica")

#]


#Ejecutar script y que nos cree la BBDD con la tabla
#micursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)", productos)

#Agregar items a la lista
#micursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'jugueteria')")

#Fuerzo un error por agregar un item con la misma KEY. Repito AR03
#micursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03', 'tren', 15, 'jugueteria')")






miconexion.commit()
miconexion.close()