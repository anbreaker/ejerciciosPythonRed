# Ejercicio 5
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al genero 
# y el nombre. El grupo A esta formado por las mujeres con un nombre anterior a 
# la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por 
# pantalla el grupo que le corresponde.

nombre = str(input('Introduce tu nombre: '))
genero = str(input('Introduce tu genero: '))
grupo = ''

if genero == 'M' and nombre.lower() < 'm' or genero == 'H' and nombre.lower() > 'n':
    grupo = 'A'
    print('Te llamas {}, tu generos es, {} y perteneces al grupo: {}'.format(nombre,genero,grupo))
else:
    grupo = 'B'
    print('Te llamas {}, tu generos es, {} y perteneces al grupo: {}'.format(nombre,genero,grupo))
