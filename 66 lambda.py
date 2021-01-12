#Lambda sirve para reusmir funciones simples como esta
#Resumir esto
def area_triangulo(base, altura):
	return(base*altura)/2

triangulo1=area_triangulo(4,8)
triangulo2=area_triangulo(5,4)

print(triangulo1)
print(triangulo2)

#en esto
area_triangulo=lambda base,altura:(base*altura)/2

triangulo1=area_triangulo(4,8)
triangulo2=area_triangulo(5,4)

print(triangulo1)
print(triangulo2)

#una forma de elevar al cubo
al_cubo=lambda numero:pow(numero,3)
print(al_cubo(13))
#otra forma de elevar al cubo
al_cubo2=lambda numero:numero**3
print(al_cubo2(13))

#otras formas. En este agregamos un signo peso al resultado
destacar_valor=lambda comision:"${}".format(comision)
comision_Ana=15858
print(destacar_valor(comision_Ana))

