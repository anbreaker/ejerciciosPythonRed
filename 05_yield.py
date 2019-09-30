def generaPares(limite):
    num = 1

    while num < limite:
        # crea un objeto iterable
        yield num * 2

        num += 1


devuelvePares = generaPares(10)

print(next(devuelvePares))

print('Aqui podria ir mas codigo...')

print(next(devuelvePares))

print('Aqui podria ir mas codigo...')

print(next(devuelvePares), '\n')


for i in devuelvePares:
    print(i)
