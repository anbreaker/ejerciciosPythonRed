from datetime import datetime

_FORMATO_FECHA = "%d-%m-%Y"
_CURRENT_DATA = datetime.now().date()


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
        if datetimeObject.year < 1920 or str(datetimeObject) > str(_CURRENT_DATA):
            print('\n\tDebes al menos haber nacido ;)\n')
            return False
        return True
    except ValueError:
        return False


def isValid(cadena):
    if not cadena[0].isalpha() or cadena[0] == 'ª' or cadena[0] == 'º':
        return False
    else:
        return True


def asignaNombreHeroe(nombre, apellidos):
    nombreSH = nombreSuperHeroes[nombre[0].upper()]
    apellidosSH = apellidoSuperHeroe[apellidos[0].upper()]
    # return nombreSH + " " + apellidosSH
    return nombreSH + " " + apellidosSH


def asignarDisfraz(fecha):
    mes = fecha.month
    superpoder = superPoderes[mes-1]
    year = fecha.year
    color = colorTraje[year % 10]
    return color, superpoder


# Pedir nombre
nombre = input('Dime tu nombre, por favor: ')
while not isValid(nombre):
    print('Nombre incorrecto debe comenzar por una de las letras del abecedario')
    nombre = input('Dime tu nombre, por favor: ')

# Pedir apellidos
apellidos = input('Dime tu primer apellido, por favor: ')
while not isValid(apellidos):
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

print("Te llamas {}, llevas un traje {} y tu superpoder es {}".format(
    nombreSuperH, colorSuperH, superPoder))
