import sqlite3

miconexion=sqlite3.connect("GestionProductos2")

micursor=miconexion.cursor()

#Creamos la tabla. Los ''' es para cuando tneemos que poner muchas columnas.
micursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50),
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

#Comento todo porque sinó se crea 2 veces.

#Creamos la lista [] con tuplas () en su interior.
productos=[

	("pelota", 20, "juguetería"),
	("pantalón", 15, "confeccion"),
	("destornillador", 25, "ferretería"),
	("jarrón", 45, "cerámica")

]


#Ejecutar script y que nos cree la BBDD con la tabla
micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

#Agregar items a la lista
#micursor.execute("INSERT INTO PRODUCTOS VALUES ('AR05', 'tren', 15, 'jugueteria')")

#Fuerzo un error por agregar un item con la misma KEY. Repito AR03
#micursor.execute("INSERT INTO PRODUCTOS VALUES ('AR03', 'tren', 15, 'jugueteria')")






miconexion.commit()
miconexion.close()