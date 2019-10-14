import datetime

today = datetime.date.today()
print(today)

birthday = datetime.date(1985, 12, 19)
print(birthday)

daysSinceBirth = (today - birthday).days
print(daysSinceBirth)


# testFecha = '4/25/2015'
# dt_obj = datetime.datetime.strptime(input, '%m/%d/%Y').month
# print(dt_obj)


# fecha = str(input('fecha '))
# if fecha is type(datetimeObject):


dia = ''
mes = ''
year = ''

fecha = '19-1s-1985'
ver = ''


def comprobarFormatoFecha(fecha):
    # if fecha
    flag = 0
    while flag == 0:
        try:
            fecha = input('Introduce una fecha ')
            formato = "%d-%m-%Y"
            datetimeObject = datetime.datetime.strptime(fecha, formato)
            dia = datetimeObject.strftime('%d')
            mes = datetimeObject.strftime('%m')
            year = datetimeObject.strftime('%Y')
            ver = f'Dia: {dia} mes {mes} año {year}'
            print(ver)
            flag = 1
        except ValueError:
            print('Escribe bien la fecha ')


comprobarFormatoFecha(fecha)
# print(type(fecha))
print('-->', ver)
