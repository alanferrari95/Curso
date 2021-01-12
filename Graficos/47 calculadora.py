from tkinter import *

raiz=Tk()
miframe=Frame(raiz)
miframe.pack()
operacion=""
resultado=0
reset_pantalla=False

#---------------------------Pantalla---------------------------
numeropan=StringVar()

pantalla=Entry(miframe, textvariable=numeropan, font=(10))
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4, sticky="W,E,N,S", ipady=10)
pantalla.config(bg="black", fg="#03f943", justify="right")

#---------------------------Pulsacion teclado---------------------------

def numeropulsado(num):
	global operacion
	global reset_pantalla
	if reset_pantalla!=False:
		numeropan.set(num)
		reset_pantalla=False
	else:

		numeropan.set(numeropan.get()+num)

#---------------------------Funcion suma---------------------------
def suma(num):
	global operacion
	global resultado
	global reset_pantalla
	resultado+=int(num)
	operacion="suma"
	reset_pantalla=True
	numeropan.set(resultado)

#---------------------------Funcion suma---------------------------

num1=0
contador_resta=0

def resta(num):
	global operacion
	global resultado
	global num1
	global contador_resta
	global reset_pantalla

	if contador_resta==0:
		num1=int(num)
		resultado=num1
	else:
		if contador_resta==1:
			resultado=num1-int(num)
		else:
			resultado=int(resultado)-int(num)
		numeropan.set(resultado)
		resultado=numeropan.get()

	contador_resta=contador_resta+1
	operacion="resta"
	reset_pantalla=True


#-------------funcion multiplicacion---------------------
contador_multi=0

def multiplica(num):

	global operacion
	global resultado
	global num1
	global contador_multi
	global reset_pantalla
	
	if contador_multi==0:
		num1=int(num)	
		resultado=num1

	else:
		if contador_multi==1:
			resultado=num1*int(num)

		else:
			resultado=int(resultado)*int(num)	

		numeropan.set(resultado)		
		resultado=numeropan.get()


	contador_multi=contador_multi+1
	operacion="multiplicacion"
	reset_pantalla=True

#-----------------funcion division---------------------

contador_divi=0

def divide(num):

	global operacion
	global resultado
	global num1
	global contador_divi
	global reset_pantalla
	
	if contador_divi==0:
		num1=float(num)		
		resultado=num1

	else:

		if contador_divi==1:
			resultado=num1/float(num)

		else:
			resultado=float(resultado)/float(num)	

		numeropan.set(resultado)		
		resultado=numeropan.get()


	contador_divi=contador_divi+1
	operacion="division"
	reset_pantalla=True

#---------------------------Funcion el_resultado---------------------------

def el_resultado():

	global resultado
	global operacion
	global contador_resta
	global contador_multi
	global contador_divi	

	if operacion=="suma":
		numeropan.set(resultado+int(numeropan.get()))
		resultado=0

	elif operacion=="resta":
		numeropan.set(int(resultado)-int(numeropan.get()))
		resultado=0
		contador_resta=0

	elif operacion=="multiplicacion":
		numeropan.set(int(resultado)*int(numeropan.get()))
		resultado=0
		contador_multi=0

	elif operacion=="division":
		numeropan.set(int(resultado)/int(numeropan.get()))
		resultado=0
		contador_divi=0


#---------------------------Fila 1---------------------------

boton7=Button(miframe, text="7", width=6, height=2, command=lambda:numeropulsado("7"))
boton7.grid(row=2, column=1, padx=2, pady=2)
boton8=Button(miframe, text="8", width=6, height=2, command=lambda:numeropulsado("8"))
boton8.grid(row=2, column=2, padx=2, pady=2)
boton9=Button(miframe, text="9", width=6, height=2, command=lambda:numeropulsado("9"))
boton9.grid(row=2, column=3, padx=2, pady=2)
botondiv=Button(miframe, text="/", width=6, height=2, command=lambda:divide(numeropan.get()))
botondiv.grid(row=2, column=4, padx=2, pady=2)

#---------------------------Fila 2---------------------------

boton4=Button(miframe, text="4", width=6, height=2, command=lambda:numeropulsado("4"))
boton4.grid(row=3, column=1, padx=2, pady=2)
boton5=Button(miframe, text="5", width=6, height=2, command=lambda:numeropulsado("5"))
boton5.grid(row=3, column=2, padx=2, pady=2)
boton6=Button(miframe, text="6", width=6, height=2, command=lambda:numeropulsado("6"))
boton6.grid(row=3, column=3, padx=2, pady=2)
botonmult=Button(miframe, text="X", width=6, height=2, command=lambda:multiplica(numeropan.get()))
botonmult.grid(row=3, column=4, padx=2, pady=2)

#---------------------------Fila 3---------------------------

boton1=Button(miframe, text="1", width=6, height=2, command=lambda:numeropulsado("1"))
boton1.grid(row=4, column=1, padx=2, pady=2)
boton2=Button(miframe, text="2", width=6, height=2, command=lambda:numeropulsado("2"))
boton2.grid(row=4, column=2, padx=2, pady=2)
boton3=Button(miframe, text="3", width=6, height=2, command=lambda:numeropulsado("3"))
boton3.grid(row=4, column=3, padx=2, pady=2)
botonrest=Button(miframe, text="-", width=6, height=2, command=lambda:resta(numeropan.get()))
botonrest.grid(row=4, column=4, padx=2, pady=2)

#---------------------------Fila 4---------------------------

boton0=Button(miframe, text="0", width=6, height=2, command=lambda:numeropulsado("0"))
boton0.grid(row=5, column=1)
botoncoma=Button(miframe, text=",", width=6, height=2, command=lambda:numeropulsado(","))
botoncoma.grid(row=5, column=2)
botonigual=Button(miframe, text="=", width=6, height=2, command=lambda:el_resultado())
botonigual.grid(row=5, column=3)
botonsum=Button(miframe, text="+", width=6, height=2, command=lambda:suma(numeropan.get()))
botonsum.grid(row=5, column=4)







raiz.mainloop()