def leer_y_buscar():
    # utilizando with es un context manager nos
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Beatriz')
    print(f'La palabra "Beatriz" aparece {counter} veces')


def escribir():
    with open('numeros.txt', 'w') as f:
        for i in range(1, 11):
            f.write(str(i))


if __name__ == "__main__":
    leer_y_buscar()
    escribir()
