# Conjutos:
# Ejercicio 2
# Escribe un programa que tenga dos listas y que, a continuacion, cree
# las siguientes listas (en las que no debe haber repeticiones):
#   Lista de palabras que aparecen en las dos listas
#   Lista de palabras que aparecen en la primeram pero no en la segunda.
#   Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#   Lista de palabras que aparecen en ambas.

lista1 = [1,2,3,4,5,4,3,2,2,1,5]
lista2 = [4,5,6,7,8,4,5,6,7,7,8]

# Elimino los elementos repetidos de ambas listas
a = set(lista1)
b = set(lista2)

listaUnion = list(a | b)
listaSolaA = list(a -b)
listaSoloB = list(b -a)
interseccion = list(a & b)

print(f'Lista de palabras que aparecen en las dos listas {listaUnion}')
print(f'Lista de palabras que aparecen en la primeram pero no en la segunda. {listaSolaA}')
print(f'Lista de palabras que aparecen en la segunda lista, pero no en la primera. {listaSoloB}')
print(f'Lista de palabras que aparecen en ambas. {interseccion}')