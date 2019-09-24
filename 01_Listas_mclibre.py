'''Listas (1) - 1
Escriba un programa que permita crear una lista de palabras. Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista. Por último, el programa tiene que escribir la lista.

Dígame cuántas palabras tiene la lista: 3
Dígame la palabra 1: Alberto
Dígame la palabra 2: Benito
Dígame la palabra 3: Carmen
La lista creada es: ['Alberto', 'Benito', 'Carmen']
Dígame cuántas palabras tiene la lista: 0
¡Imposible!
'''

numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
    print("La lista creada es:", lista)