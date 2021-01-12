from io import open

archivo_texto=open("archivo.txt","r+") #lectura y escritura

#print(archivo_texto.read())
#Se posiciona en la posicion 0
#archivo_texto.seek(0)
#print(archivo_texto.read())

lista_texto=archivo_texto.readlines()
lista_texto[1]="Esta linea fue modificada desde el exterior\n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()


