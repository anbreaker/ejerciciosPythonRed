lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# Elimino los elementos repetidos de ambas listas
a = set(lista1)
b = set(lista2)

listaUnion = list(a | b)
solaA = list(a -b)
soloB = list(b -a)
interseccion = list(a & b)

