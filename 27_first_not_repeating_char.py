# construir un programa que nos permita encontrar el primer carácter que no se repite en un string.
# Por ejemplo si tenemos el string mimamameama el primer carácter que no se repite es la i.

# "abacabad" --> c
# "abacabaabacaba" --> todo se repite
# "abcdefghijklmnopqrstuvwxyziflskecznslkjfabe" --> d
# "bcccccccccccccyb" --> y


def first_not_repeating_char(char_sequence):
    char_enter = {}

    for index, letter in enumerate(char_sequence):
        if letter not in char_enter:
            char_enter[letter] = (index, 1)
        else:
            char_enter[letter] = (char_enter[letter][0], char_enter[letter][1] + 1)

        final_letters = []
        for key, value in char_enter.items():
            if value[1] == 1:
                final_letters.append((key, value[0]))

    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    if not_repeated_letters:
        return not_repeated_letters[0][0]
    else:
        return -1


if __name__ == '__main__':
    char_sequence = str(input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == -1:
        print('Todos los caracteres se repiten.')
    else:
        print(f'El primer caracter no repetido es: {result}')
