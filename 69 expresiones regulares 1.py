import re

cadena="Vamos a aprender expresiones regulares en Python. Python es un lenguaje sencillo"

textobuscar="Python"

'''if re.search(textobuscar, cadena) is not None:
	print("He encontrado el texto")

else:
	print("No he encontrado el texto")



textencontrado=re.search(textobuscar, cadena)

print(textencontrado.start())
print(textencontrado.end())
print(textencontrado.span())'''
print(len(re.findall(textobuscar, cadena)))

