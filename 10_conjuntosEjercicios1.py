# Conjutos:
# Ejercicio 2
# Escribe un programa que tenga dos listas y que, a continuacion, cree
# las siguientes listas (en las que no debe haber repeticiones):
#   Lista de palabras que aparecen en las dos listas
#   Lista de palabras que aparecen en la primeram pero no en la segunda.
#   Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#   Lista de palabras que aparecen en ambas.

mensaje1 = 'Hola mundo Elvas Badajoz 1 2 3 4 Lorem the printing and typesetting industry.'
mensaje2 = 'Lorem Lorem Ipsum is simply dummy text of simply the printing and typesetting industry.'


lista1 = mensaje1.split(' ')
lista2 = mensaje2.split(' ')
# print(lista1)
# print(lista2)

conjunto1 = set(lista1)
conjunto2 = set(lista2)
listaConjunta = conjunto1 | conjunto2
print('')
print(conjunto1)
print(conjunto2)
print('')
print(listaConjunta)
print('')
