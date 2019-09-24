# Ejercicio 4
# Escribir un programa que pregunte el nombre del usuario en la consola
# y un número entero e imprima por pantalla en líneas distintas el nombre 
# del usuario tantas veces como el número introducido.

nombre = input('¿Cual es tu nombre? ')
numVeces = int(input('¿Cuantas veces lo quieres ver por pantalla? '))

print ((nombre + '\n') * numVeces)


# while numVeces > 0:
#   print(nombre)
#   numVeces -= 1
