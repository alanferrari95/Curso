from tkinter import *
from tkinter import messagebox

root=Tk()

def infoadicional():
	messagebox.showinfo("Procesador de Alan", "Procesador de texto version 2020")

def avisolicencia():
	messagebox.showwarning("Licencia", "Producto bajo licencia GNU")

def saliraplicacion():
	#esto devuelve Si o No
	#valor=messagebox.askquestion("Salir", "¿Deseas salir de la aplicación?")

	#Esto devuelve aceptar o cancelar
	valor=messagebox.askokcancel("Salir", "¿Deseas salir de la aplicación?")

	if valor==True:
		root.destroy()

def cerrardocumento():
	valor=messagebox.askretrycancel("Reintentar", "No es posible cerrar. Documetno bloqueado")	

	if valor==False:
		root.destroy()

barramenu=Menu(root)
root.config(menu=barramenu, width=300, height=300)

archivomenu=Menu(barramenu, tearoff=0)
archivomenu.add_command(label="Nuevo")
archivomenu.add_command(label="Guardar")
archivomenu.add_command(label="Guardar como")
archivomenu.add_separator()
archivomenu.add_command(label="Cerrar", command=cerrardocumento)
archivomenu.add_command(label="Salir", command=saliraplicacion)

archivoedicion=Menu(barramenu, tearoff=0)
archivoedicion.add_command(label="Copiar")
archivoedicion.add_command(label="Cortar")
archivoedicion.add_command(label="Pegar")

archivoherramientas=Menu(barramenu, tearoff=0)

archivoayuda=Menu(barramenu, tearoff=0)
archivoayuda.add_command(label="Licencia", command=avisolicencia)
archivoayuda.add_command(label="Acerca de", command=infoadicional)

barramenu.add_cascade(label="Archivo", menu=archivomenu)
barramenu.add_cascade(label="Edicion", menu=archivoedicion)
barramenu.add_cascade(label="Herramientas", menu=archivoherramientas)
barramenu.add_cascade(label="Ayuda", menu=archivoayuda)





root.mainloop()