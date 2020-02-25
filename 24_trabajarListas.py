# unir listas (+)
lista = [1, 2, 3]

lista_2 = [4, 5, 6]
lista_3 = lista + lista_2
lista.extend(lista_2)

print(f'Unir listas: {lista_3}')
print(f'Unir listas: {lista}')

# Multiplicar elementos
lista_4 = [5]
lista_5 = lista_4 * 10
print(f'multiplicar elementos {lista_5}')
"""los operadores /(division) y -(resta) no puede utilizarse en cuando tenemos el tipo list
las listas soportan el operador de slices [:::]. punto de inicio, punto final y opcional de cada cuantos pasos."""

# indice uno hasta 3
lista_6 = lista_3[1:3]
print(f'index 1 hasta el 3: {lista_6}')

# indice uno hasta 3 de 2 en 2
lista_7 = lista_3[0:6:2]
print(f'index 0 hasta el 6 de 2 en 2: {lista_7}')

# desde el inicio hasta el final invertida
lista_8 = lista_3[::-1]
print(f'Desde el inicio hasta el final invertida: {lista_8}')

# anadir elemento al final de la lista
lista_8.append(9)
print(f'Añadir elememto{lista_8}')

# Eliminar ultimo elemento de la lista y lo devuelve
numero_devuelto = lista_8.pop()
print(f'Eliminar ultimo elememto{lista_8}, el numero devuelto es: {numero_devuelto}')

# Elimina el elemento de la poscion 'x' de la lista y lo devuelve
elemento_eliminado = lista_8.pop(2)
print(f'Eliminar elememto selecionado {lista_8}, el elemento eliminado es {elemento_eliminado}')

listaDesordenada = [5, 7, 9, 2, 1, 4, 3]
listaDesordenada.sort()
print(f'Ordenar lista: {listaDesordenada}')

# Eliminar elemento de la lista
utiles = ['borrador', 'lapiz', 'ega', 'cuaderno']
del utiles[2]
print(utiles)

# guardar un str en una lista
palabras = 'palabras'
lista_palabras = list(palabras)
print(lista_palabras)
