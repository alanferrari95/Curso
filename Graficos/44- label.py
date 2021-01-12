#imagenes y texto

from tkinter import *

root=Tk()

miframe=Frame(root, width=500, height=400)

miframe.pack()

Label(miframe, text="Hola alumnos de python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)




root.mainloop()