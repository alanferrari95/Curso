from tkinter import *

raiz=Tk()

miframe=Frame(raiz, width=1200, height=600)
miframe.pack()

minombre=StringVar()

#lo que va entre parentesis es el contenedor padre
cuadronombre=Entry(miframe, textvariable=minombre)
cuadronombre.grid(row=0, column=1, padx=5, pady=5)

cuadroapellido=Entry(miframe)
cuadroapellido.grid(row=1, column=1, padx=5, pady=5)

cuadrodireccion=Entry(miframe)
cuadrodireccion.grid(row=2, column=1, padx=5, pady=5)

cuadropass=Entry(miframe)
cuadropass.grid(row=3, column=1, padx=5, pady=5)
cuadropass.config(show="*")

textocomentario=Text(miframe, width=15, height=5)
textocomentario.grid(row=4, column=1, padx=5, pady=5)

scroll=Scrollbar(miframe, command=textocomentario.yview)
scroll.grid(row=4, column=2, sticky="nsew")
textocomentario.config(yscrollcommand=scroll.set)


nombrelabel=Label(miframe, text="Nombre: ")
nombrelabel.grid(row=0, column=0, sticky="w", padx=5, pady=5)

apellidolabel=Label(miframe, text="Apellido: ")
apellidolabel.grid(row=1, column=0, sticky="w", padx=5, pady=5)

direccionlabel=Label(miframe, text="Direccion: ")
direccionlabel.grid(row=2, column=0, sticky="w", padx=5, pady=5)

passlabel=Label(miframe, text="Password: ")
passlabel.grid(row=3, column=0, sticky="w", padx=5, pady=5)

comentariolabel=Label(miframe, text="Comentarios: ")
comentariolabel.grid(row=4, column=0, sticky="w", padx=5, pady=5)

def codigoboton():
	minombre.set("Alan")

botonenvio=Button(raiz, text="Enviar", command=codigoboton)
botonenvio.pack()




raiz.mainloop()