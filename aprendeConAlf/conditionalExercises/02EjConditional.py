# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña
# en una variable, pregunte al usuario por la contraseña e imprima por 
# pantalla si la contraseña introducida por el usuario coincide con la 
# guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = 'contraseña'
password = str(input('Introduzca su contraseña '))
if key == password.lower():
    print('Contraseña correcta --> {}'.format(password))
else:
    print('Contraseña incorrecta')