from tkinter import *


root=Tk()

root.title("Ejemplo")

playa=IntVar()
montana=IntVar()
turismo=IntVar()

def opcionesviaje():
	opcionescogida=""

	if (playa.get()==1):
		opcionescogida+="Playa "
	if (montana.get()==1):
		opcionescogida+="Montaña "
	if (turismo.get()==1):
		opcionescogida+="Turismo "

	textofinal.config(text=opcionescogida)

frame=Frame(root)
frame.pack()

Label(frame, text="Elige destinos", width=50).pack()

Checkbutton(frame, text="Playa", variable=playa, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(frame, text="Montaña", variable=montana, onvalue=1, offvalue=0, command=opcionesviaje).pack()
Checkbutton(frame, text="Turismo", variable=turismo, onvalue=1, offvalue=0, command=opcionesviaje).pack()

textofinal=Label(frame)
textofinal.pack()

root.mainloop()