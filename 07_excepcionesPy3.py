import math


def evaluaEdad(edad):
    if edad < 0:
        # Lanzamiento de errores propios
        raise TypeError('No existen Edades negativas')

    if edad < 20:
        return 'Eres muy joven '
    elif edad < 40:
        return "Eres joven "
    elif edad < 65:
        return 'Eres maduro'
    elif edad < 100:
        return 'Cuidate...'

# print(evaluaEdad(-18))


def calcularRaiz(num1):
    if num1 < 0:
        raise ValueError('El Nº no puede ser Negativo ')
    else:
        return math.sqrt(num1)


op1 = int(input('Introduce un numero: '))

try:
    print(calcularRaiz(op1))
except ValueError as errorDeNumeroNegativo:
    print('errorDeNumeroNegativo')

print('Fin del Programa.')
