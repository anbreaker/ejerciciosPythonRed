def factorial(numero):
    if numero == 1:
        return numero
    elif numero <= 0:
        print('Debe se un numero entero positivo mayor de 0')
    else:
        return numero * factorial(numero-1)


if __name__ == '__main__':
    numero = int(input('Escribe un número: '))

    resultado = factorial(numero)

    print(resultado)
