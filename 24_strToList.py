# unir listas (+)
lista = [1, 2, 3]

listaDos = [4, 5, 6]
listaTres = lista + listaDos
lista.extend(listaDos)

print(f'Unir listas: {listaTres}')
print(f'Unir listas: {lista}')

# Multiplicar elementos
listaCuatro = [5]
listaCinco = listaCuatro * 10
print(f'multiplicar elementos {listaCinco}')
"""los operadores /(division) y -(resta) no puede utilizarse en cuando tenemos el tipo list
las listas soportan el operador de slices [:::]. punto de inicio, punto final y opcional de cada cuantos pasos."""

# indice uno hasta 3
listaSeis = listaTres[1:3]
print(f'index 1 hasta el 3: {listaSeis}')

# indice uno hasta 3 de 2 en 2
listaSiete = listaTres[0:6:2]
print(f'index 0 hasta el 6 de 2 en 2: {listaSiete}')

# desde el inicio hasta el final invertida
listaOcho = listaTres[::-1]
print(f'Desde el inicio hasta el final invertida: {listaOcho}')

# anadir elemento al final de la lista
listaOcho.append(9)
print(f'Añadir elememto{listaOcho}')

# Eliminar ultimo elemento de la lista y lo devuelve
numero_devuelto = listaOcho.pop()
print(f'Eliminar ultimo elememto{listaOcho}, el numero devuelto es: {numero_devuelto}')

# Elimina el elemento de la poscion 'x' de la lista y lo devuelve
elemento_eliminado = listaOcho.pop(2)
print(f'Eliminar elememto selecionado {listaOcho}, el elemento eliminado es {elemento_eliminado}')

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
