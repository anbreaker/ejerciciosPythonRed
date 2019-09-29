from datetime import datetime, timedelta

current_data = datetime.now()
print('Hoy es: ' + str(current_data))


print('Dia: ' + str(current_data.day))
print('Mes: ' + str(current_data.month))
print('Año: ' + str(current_data.year))
print('Hora: ' + str(current_data.hour))
print('Minutos: ' + str(current_data.minute))
print('Segundos: ' + str(current_data.second))


# timedelta is used to define a period of time
today = datetime.now()
one_day = timedelta(days=1)
yerterday = today - one_day
print('Yesterday was: ' + str(yerterday))

birthday = input('Cuando es tu cumpleaños (dd/mm/yyy) ')
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')
print('Cumpleaños: ' + str(birthday_date))
