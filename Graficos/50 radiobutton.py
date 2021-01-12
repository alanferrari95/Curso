from tkinter import *

root=Tk()

varopcion=IntVar()

def imprimir():
	#print(varopcion.get())
	if varopcion.get()==1:
		etiqueta.config(text="Has elegido masculino")
	elif varopcion.get()==2:
		etiqueta.config(text="Has elegido femenino")
	else:
		etiqueta.config(text="Has elegido otros")

Label(root, text="Género:").pack()

Radiobutton(root, text="Masculino", variable=varopcion, value=1, command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=varopcion, value=2, command=imprimir).pack()
Radiobutton(root, text="Otro", variable=varopcion, value=3, command=imprimir).pack()


etiqueta=Label(root)
etiqueta.pack()




root.mainloop()