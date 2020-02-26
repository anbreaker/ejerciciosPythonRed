import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

LIST_PALABRAS = [
    'lavadora',
    'secadora',
    'sofa',
    'españa',
    'portugal',
    'motos',
    'teclado'
]


def palabra_random():
    index = random.randint(0, len(LIST_PALABRAS)-1)
    return LIST_PALABRAS[index]


def pantalla(palabra_escondida, intentos):
    print(IMAGES[intentos])
    print('')
    print(palabra_escondida)
    print('--- * --- *--- * --- *--- * --- ')


def run():
    palabra = palabra_random()
    palabra_escondida = ['_'] * len(palabra)
    intentos = 0

    while True:
        pantalla(palabra_escondida, intentos)
        entra_letra = str(input('Escoge una letra: '))
        
        letra_index = []
        for i in range(len(palabra)):
            if palabra[i] == entra_letra:
                letra_index.append(i)
                
        if len(letra_index) == 0:
            intentos += 1
            
            if intentos == 7:
                pantalla(palabra_escondida,intentos)
                print(f'\n Perdiste la palabra era {palabra}')
                break            
        else:
            for i in letra_index:
                palabra_escondida[i] = entra_letra
            letra_index = []
            
            try:
                palabra_escondida.index('_')                
            except ValueError:
                print('Ganaste')
                break


if __name__ == '__main__':
    print(' B I E N B E N I D O S  -A-  A H O R C A D O S')
    run()
