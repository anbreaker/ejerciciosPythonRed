# Ejercicio: Eliminar los elementos repetidos de una lista
# Los conjutos se inician con set()

lista = [1, 2, 3, 'hola', 2, 1, 3, 1, 2, 'hola', 3]

conjunto = set(lista)

print('Ver si un valor esta contenido en el conjunto--> ', 1 in conjunto)

# agregando valores
conjunto.add('a')
conjunto.add(5)
conjunto.discard(3)  # Para elimnar algun elemento del conjuto
lista = list(conjunto)

print(f'lista completa --> {lista}')
print(f'Conjunto --> {conjunto}')
print(f'Lista sin elementos repetidos --> {lista}')

# Todo en una linea:
lista = print('Ejecicio en un alinea--> ', list(set(lista)))

mensaje = 'Lorem Lorem Ipsum is simply dummy text of simply the printing and typesetting industry.'
listaMensaje = mensaje.split(' ')
print(listaMensaje)
conjuntoMensaje = list(set(listaMensaje))
print(conjuntoMensaje)
