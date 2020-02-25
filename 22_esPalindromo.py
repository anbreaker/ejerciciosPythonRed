palindromo = input('Introduce una frase para comprobar si es palindromo: ')


def esPalindromo(palindromo):
    comparar_palindromo = palindromo.lower().replace(' ', '')
    if comparar_palindromo == comparar_palindromo[::-1]:
        print('Es un Palindromo')
    else:
        print('No es Palindromo')


if __name__ == '__main__':
    esPalindromo(palindromo)
