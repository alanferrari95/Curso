import sqlite3

miconexion=sqlite3.connect("GestionProductos3")

micursor=miconexion.cursor()

#UNIQUE hace que no se pueda generar 2 valores con el mismo nombre
micursor.execute('''
	CREATE TABLE PRODUCTOS (
	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	NOMBRE_ARTICULO VARCHAR(50) UNIQUE,
	PRECIO INTEGER,
	SECCION VARCHAR(20))
''')

productos=[

	("pelota", 20, "juguetería"),
	("pantalón", 15, "confeccion"),
	("destornillador", 25, "ferretería"),
	("jarrón", 45, "cerámica"),
	("pantalónes", 35, "confeccion")

]


micursor.executemany("INSERT INTO PRODUCTOS VALUES (NULL,?,?,?)", productos)

miconexion.commit()
miconexion.close()