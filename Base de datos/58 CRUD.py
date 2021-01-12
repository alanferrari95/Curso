import sqlite3

miconexion=sqlite3.connect("GestionProductos3")

micursor=miconexion.cursor()

#CRUD: CREATE, READ, UPDATE (actualizar), DELETE

#READ: Ver articulos de seccion
micursor.execute("SELECT * FROM PRODUCTOS WHERE SECCION='confeccion'")

#READ: fetchall sirve para leer.
productos=micursor.fetchall()
print(productos)

#UPDATE: actualizar el precio a $15
#micursor.execute("UPDATE PRODUCTOS SET PRECIO=15 WHERE NOMBRE_ARTICULO='pelota'")

#DELETE: borrar algún articulo
#micursor.execute("DELETE FROM PRODUCTOS WHERE ID=5")


miconexion.commit()
miconexion.close()