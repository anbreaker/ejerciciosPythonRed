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


def validarEntradaAlpha(opcion):
    flag = 0
    while flag == 0:
        try:
            entrada = str(input(f'Introduce tu {opcion}: '))
            entrada = entrada.upper()
            entrada = entrada.split()
            primeraParteDeLaEntrada = str(entrada[0])
            primeraLetraDeLaEntrada = str(primeraParteDeLaEntrada[0])
            if not primeraLetraDeLaEntrada.isalpha() or primeraLetraDeLaEntrada == 'ª' or primeraLetraDeLaEntrada == 'º':
                print('\n¡Warning, ¡Warning!\n')
            else:
                flag = 1
            # Prueba
            print(f'{nombreSuperHeroes[primeraLetraDeLaEntrada]}')
        except IndexError:
            print(f'\nDebes escribir un {opcion}: ')
        except KeyError:
            print(f'Tu {opcion} debe comenzar por letras del alfabeto')


validarEntradaAlpha('Apellido')

fecha = '19-1s-1985'
ver = ''


def comprobarFormatoFecha(fecha):
    flag = 0
    while flag == 0:
        try:
            fecha = input('Introduce una fecha (dd-mm-yyyy)')
            formato = "%d-%m-%Y"
            datetimeObject = datetime.datetime.strptime(fecha, formato)
            dia = datetimeObject.strftime('%d')
            mes = datetimeObject.strftime('%m')
            year = datetimeObject.strftime('%Y')
            ver = f'Dia: {dia} mes {mes} año {year}'
            print(ver)
            flag = 1
        except ValueError:
            print('Escribe bien el formato de fecha (dd-mm-yyyy)')


comprobarFormatoFecha(fecha)
