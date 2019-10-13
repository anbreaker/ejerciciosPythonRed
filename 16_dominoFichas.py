# Las fichas de dominó se pueden enumerar como se indican en la siguiente lista:
#   a) Para el ejercicio anterior, realizar un programa que dado el número asignado nos
#      devuelva los valores de arriba y abajo.
#   b) Escribir un programa que dado los valores de la ficha de dominó (arriba y abajo)
#      nos devuelva el valor asignado.

fichasDomino = {0: '0.0', 1: '0.1', 2: '0.2', 3: '0.3', 4: '0.4', 5: '0.5', 6: '0.6', 7: '1.1',
                8: '1.2', 9: '1.3', 10: '1.4', 11: '1.5', 12: '1.6', 13: '2.2', 14: '2.3', 15: '2.4',
                16: '2.5', 17: '2.6', 18: '3.3', 19: '3.4', 20: '3.5', 21: '3.6', 22: '4.4',
                23: '4.5', 24: '4.6', 25: '5.5', 26: '5.6', 27: '6.6'}

mensaje = 'Las fichas de dominó se pueden enumerar como se indican en la siguiente lista:'
opcion1 = '\t1) Opcion 1 dado el número asignado nos devuelva los valores de ficha.'
opcion2 = '\t2) Opcion 2 dado los valores de la ficha de dominó (arriba y abajo) nos devuelva el valor asignado.'
opcion = 0

while opcion == 0:
    print(f'{mensaje} \n\t{fichasDomino}')
    print(f'{opcion1} \n{opcion2}')
    elegirOpcion = int(input('Elige la opcion 1 o 2: '))
    if elegirOpcion == 1:
        verValor = int(input('Introduce el Nº de ficha que deseas ver: '))
        print(f'La ficha tiene el valor --> {fichasDomino[verValor]}')
        opcion = 1
    if elegirOpcion == 2:
        valor = str(
            input('Introduce el Nº de ficha que deseas ver: (Formato EJ: 1.6) '))
        buscando = list(fichasDomino.keys())[
            list(fichasDomino.values()).index(valor)]
        print(buscando)
        opcion = 1


# claves = list(fichasDomino.keys())
# valores = list(fichasDomino.values())
# print(f'\nClaves --> {claves} \n')
# print(f'Valores -> {valores}')
