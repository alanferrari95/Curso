from tkinter import *

raiz=Tk()

raiz.title("Ventaja de prueba")

#True,False para ancho,alto.
#raiz.resizable()

#Cambiar icono del programa
raiz.iconbitmap("descarga.ico")

#Otra forma de cambiar el ancho y largo
#raiz.geometry("650x350")

#Cambiar color de fondo
raiz.config(bg="blue")

#creamos el Frame
miframe=Frame()

#Incluimos el frame en la raiz
miframe.pack(fill="both", expand="True")

#color de fondo del frame
miframe.config(bg="white")

#tamaño del frame
miframe.config(width="650", height="350")

#mainloop bucle infinito. SIEMPRE tiene que estar al final.
raiz.mainloop()