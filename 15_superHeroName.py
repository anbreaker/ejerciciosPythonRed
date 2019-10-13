import datetime

# Haz un programa que te pida nombre completo y fecha de nacimiento.
# Y según ello te de tu nombre de superhéroe, tus poderes, tu color de traje y tu arma.
# Deberas valorar que la fecha es correcta formalmente y también que el usuario ha nacido antes de hoy.
# Una vez lo tengas para consola, puedes intentarlo con tkinter.

# 1: NOMBRE DE SUPERHÉROE
# Busca la Primera inicial de tu nombre y apellido
nombreSuperHeroes = {'A': 'Sobaco', 'B': 'Asesino', 'C': 'Capitan', 'D': 'Pezon',
                     'E': 'Trueno', 'F': 'Lobo', 'G': 'Conejo', 'H': 'Halcón',
                     'I': 'Sargento', 'J': 'Principe', 'K': 'El Milagro',
                     'L': 'El Rey', 'M': 'Maestro', 'N': 'Robot', 'O': 'Vigilante',
                     'P': 'Avispa', 'Q': 'Doctor', 'R': 'Orificio', 'S': 'Fantasma',
                     'T': 'Prepucio', 'U': 'Tiburon', 'V': 'Aguijon', 'W': 'Pepino',
                     'X': 'Agente', 'Y': 'Tornado', 'Z': 'Brujo'}

# Ahora la primera inicial de tu Apellido.
apellidoSuperHeroe = {'A': 'Elastico', 'B': 'Carmesi', 'C': 'Radiactivo', 'D': 'Volador', 'E': 'Espacial',
                      'F': 'Letal', 'G': 'Flácido', 'H': 'Marciano', 'I': 'Venenoso', 'J': 'Invisilbe',
                      'K': 'Mutante', 'L': 'Vengador', 'M': 'Amoroso', 'N': 'Apestoso', 'O': 'Mágico',
                      'P': 'Gigante', 'Q': 'Nazi', 'R': 'Biónico', 'S': 'Celestial', 'T': 'Sangriento',
                      'U': 'Rocoso', 'V': 'De Hierro', 'W': 'Psíquico', 'X': 'Maravilla', 'Y': 'Hipster',
                      'Z': 'Invencible'}

# 2: El COLOR DE TU TRAJE
# Escoge el último número del año en el que naciste.
colorTraje = {'0': 'Escarlata', '1': 'Dorado', '2': 'Amarillo', '3': 'Oscuro', '4': 'Verde',
              '5': 'Blanco', '6': 'Azul', '7': 'Gris', '8': 'Plateado', '9': 'Rojo'}

# 3: SUPERPODERES
# Busca el número del mes en el que naciste.
superPoderes = {'1': 'Convertir todo en Algodón', '2': 'Velocidad de la luz', '3': 'Hablar con los animales',
                '4': 'Super Fuerza', '5': 'Control Mental', '6': 'Invisibilidad', '7': 'Control del Fuego',
                '8': 'Crear Tormentas', '9': 'Convertir el agua en Cerveza', '10': 'Destruir Planetas',
                '11': 'Saltar 20 Metros', '12': 'Volar'}


flag = 0
# nombre = str(input('Introduce tu nombre: '))
nombre = 'fj'
# apellido = str(input('Introduce tu apellido: '))
apellido = 'an'
# birthYear = str(input('Año de nacimiento: '))

# fechaNacimiento = str(input('Introduce Fecha Nacimiento (dd-mm-aaaa) '))

fechaNacimiento = '12-03-1993'
formatoFecha = '%d-%m-%Y'

datetimeObject = datetime.datetime.strptime(fechaNacimiento, formatoFecha)
dia = str(datetimeObject.strftime('%d'))
mes = str(datetimeObject.strftime('%m'))
year = str(datetimeObject.strftime('%Y'))


while flag == 0:

    if nombre.isalpha() and apellido.isalpha() and dia.isalnum() and mes.isalnum() and year.isalnum():
        flag = 1
        # nombre:
        nombre = nombre.upper()
        primeraLetraNombre = nombre[0]

        # apellido
        apellido = apellido.upper()
        primeraLetraApellido = apellido[0]

        # Mes Nacimiento
        mes = mes[-1]
        # Año Nacimiento
        year = year[-1]

        # Mensaje de salida
        print(
            f'Tu Nombre de superheroes es:\n\t{nombreSuperHeroes[primeraLetraNombre]} {apellidoSuperHeroe[primeraLetraApellido]} llevas un traje de color {colorTraje[year]} y tu superPoder es: {superPoderes[mes]}')

    else:
        if nombre.isalpha():
            apellido = str(
                input('Introduce tu apellido: (Caracteres Alfabeticos)'))
        elif apellido.isalpha():
            nombre = str(
                input('Introduce tu nombre: (Caracteres Alfabeticos)'))
        else:
            nombre = str(
                input('Introduce tu nombre: (Caracteres Alfabeticos)'))
            apellido = str(
                input('Introduce tu apellido: (Caracteres Alfabeticos)'))
            fechaNacimiento = str(
                input('Introduce Fecha Nacimiento en este formato: (dd-mm-aaaa) '))
