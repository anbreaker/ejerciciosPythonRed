import random


def run():
    numero_encontrado = False
    numero_random = random.randint(0, 20)

    while not numero_encontrado:
        number = int(input('Intenta un número：'))

        if number == numero_random:
            print('Felicidades. Encontraste el número')
            numero_encontrado = True
        elif number > numero_random:
            print('El número es más pequeño')
        else:
            print('El número es más grande')


if __name__ == '__main__':
    run()
