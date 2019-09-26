# Ejercicio 3
# Escribir un programa que pida al usuario un número entero positivo y muestre 
# por pantalla todos los números impares desde 1 hasta ese número separados por comas.

numero = int(input('Introduce un Nº entero: '))

for i in range (numero):
    if i % 2 != 0:
        print(f'{i}', end=', ')
    