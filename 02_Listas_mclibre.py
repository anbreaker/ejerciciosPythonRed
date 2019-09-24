'''
El usuario escribira una lista de palabras, para terminar, escribira 'terminar' o 't'
Una vez terminado se mostraran las palabra de la lista.
Enumerar las palabras introducidas mienstras se va rellenando la lista
'''

lista = []
palabra = ''
contador = 0
while(palabra != 'terminar' and palabra != 't'):
    contador += 1
    print("Escriba Palabras", str(contador) + ": ", end="")
    palabra = input()
    if (palabra != 'terminar' and palabra != 't'):
        lista += [palabra]
print("La lista creada es: {} y tiene posiciones".format(lista))