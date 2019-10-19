from datetime import datetime

_FORMATO_FECHA = "%d-%m-%Y"
_CURRENT_DATA = datetime.now().date()
_POSIBLE_VALOR_ENTRADA = 'áéíóúüçÇÁÉÍÓÚ'
_SALIDA = 'aeiouuzZAEIOU'


nombreSuperHeroes = {'A': 'Sobaco', 'B': 'Asesino', 'C': 'Capitan', 'D': 'Pezon', 'E': 'Trueno', 'F': 'Lobo', 'G': 'Conejo', 'H': 'Halcon',
                     'I': 'Sargento', 'J': 'Principe', 'K': 'El Milagro', 'L': 'El Rey', 'M': 'Maestro', 'N': 'Robot', 'O': 'Vigilante',
                     'P': 'Avispa', 'Q': 'Doctor', 'R': 'Orificio', 'S': 'Fantasma', 'T': 'Prepucio', 'U': 'Tiburon', 'V': 'Aguijon', 'W': 'Pepino',
                     'X': 'Agente', 'Y': 'Tornado', 'Z': 'Brujo'}

apellidoSuperHeroe = {'A': 'Elastico', 'B': 'Carmesi', 'C': 'Radiactivo', 'D': 'Volador', 'E': 'Espacial',
                      'F': 'Letal', 'G': 'Flacido', 'H': 'Marciano', 'I': 'Venenoso', 'J': 'Invisilbe',
                      'K': 'Mutante', 'L': 'Vengador', 'M': 'Amoroso', 'N': 'Apestoso', 'O': 'Magico',
                      'P': 'Gigante', 'Q': 'Nazi', 'R': 'Bionico', 'S': 'Celestial', 'T': 'Sangriento',
                      'U': 'Rocoso', 'V': 'De Hierro', 'W': 'Psiquico', 'X': 'Maravilla', 'Y': 'Hipster',
                      'Z': 'Invencible'}

colorTraje = ['Escarlata', 'Dorado', 'Amarillo', 'Oscuro',
              'Verde', 'Blanco', 'Azul', 'Gris', 'Plateado', 'Rojo']

superPoderes = ['Convertir todo en Algodon', 'Velocidad de la luz', 'Hablar con los animales', 'Super Fuerza', 'Control Mental', 'Invisibilidad',
                'Control del Fuego', 'Crear Tormentas', 'Convertir el agua en Cerveza', 'Destruir Planetas', 'Saltar 20 Metros', 'Volar']


def validarFecha(cadena):
    try:
        datetimeObject = datetime.strptime(cadena, _FORMATO_FECHA)
        if str(datetimeObject) > str(_CURRENT_DATA):
            print('\n\tDebes al menos haber nacido ;)\n')
            return False
        elif datetimeObject.year < 1920:
            print('¿Seguro que sigues vivo? ;)')
            return False
        return True
    except ValueError:
        return False


def convertirAcentos(cadena):
    cambiarAcentos = str.maketrans(_POSIBLE_VALOR_ENTRADA, _SALIDA)
    cadena = nombre.translate(cambiarAcentos)
    return cadena


def esValida(cadena):
    if not cadena[0].isalpha() or cadena[0] == 'ª' or cadena[0] == 'º':
        return False
    else:
        return True


def asignaNombreHeroe(nombre, apellido):
    nombreSinAcentos = convertirAcentos(nombre)
    nombreSH = nombreSuperHeroes[nombreSinAcentos[0].upper()]
    apellidoSinAcento = convertirAcentos(apellido)
    apellidosSH = apellidoSuperHeroe[apellidoSinAcento[0].upper()]
    # return nombreSH + " " + apellidosSH
    return (f'{nombreSH} {apellidosSH}')


def asignarDisfraz(fecha):
    mes = fecha.month
    superpoder = superPoderes[mes-1]
    year = fecha.year
    color = colorTraje[year % 10]
    return color, superpoder


# Pedir nombre
nombre = input('Dime tu nombre, por favor: ')
while not esValida(nombre):
    print('Nombre incorrecto debe comenzar por una de las letras del abecedario')
    nombre = input('Dime tu nombre, por favor: ')

# Pedir apellidos
apellidos = input('Dime tu primer apellido, por favor: ')
while not esValida(apellidos):
    print('Apellido incorrecto debe comenzar por una de las letras del abecedario')
    apellidos = input('Dime tu primer apellido, por favor: ')

# Pedir fecha
fecha = input('Dime tu fecha de nacimiento (dd-mm-yyyy): ')
while not validarFecha(fecha):
    print('Debes introducir una fecha correcta, con el formato dd-mm-yyyy')
    fecha = input('Dime tu fecha de nacimiento (dd-mm-yyyy): ')

# Asignaciones
fecha = datetime.strptime(fecha, _FORMATO_FECHA)
nombreSuperH = asignaNombreHeroe(nombre, apellidos)
colorSuperH, superPoder = asignarDisfraz(fecha)

print(
    f'Te llamas {nombreSuperH}, llevas un traje {colorSuperH} y tu superpoder es {superPoder}')
