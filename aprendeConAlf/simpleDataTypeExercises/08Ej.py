# Ejercicio 8
# Escribir un programa que pida al usuario dos números enteros y muestre 
# por pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde 
# <n> y <m> son los números introducidos por el usuario, y <c> y <r> 
# son el cociente y el resto de la división entera respectivamente.

dividendo = int(input('Introduce el dividendo: '))
divisor = int(input('Introduce el divisor: '))

cociente = int(dividendo / divisor)
resto = dividendo % divisor
print('El cociente es: {}'.format(cociente))
print('El resto de la division es: {}'.format(resto))