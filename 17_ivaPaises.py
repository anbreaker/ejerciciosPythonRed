# Aplicando IVA general por paises:
# Según el pais se aplica un tipo general de IVA u otro.
# Haz un programa que aplique el tipo de IVA adecuado según el pais de origen
#   Seguir la siguiente tabla:
#     https://getquipu.com/blog/wp-content/uploads/2014/08/Artboard-asypv.png
#     El programa debe mostrar la base, el iva aplicado en % y en € y el precio final.
#       # Restricciones: Las cantidades en € deben aparecer ajustadas al céntimo.
#       # Utilizar una sola instrucción de impresión de resultados

_POSIBLE_VALOR_ENTRADA = 'áéíóúüçÇÁÉÍÓÚ'
_SALIDA = 'aeiouuzZAEIOU'

ivaPaises = {
    'Hungria': 27, 'Croacia': 25, 'Dinamarca': 25, 'Suecia': 25, 'Finlandia': 24,
    'Bulgaria': 20, 'Eslovaquia': 20, 'Estonia': 20, 'Francia': 20, 'Malta': 18,
    'Rumania': 24, 'Grecia': 23, 'Irlanda': 23, 'Polonia': 23, 'Portugal': 23,
    'Eslovenia': 22, 'Italia': 22, 'España': 21, 'Belgica': 21, 'Letonia': 21,
    'Lituania': 21, 'Paises Bajos': 21, 'Republica Checa': 21, 'Austria': 20,
    'Reino Unido': 20, 'Alemania': 19, 'Chipre': 19, 'Luxemburgo': 15
}


def convertirAcentosTitle(nombre):
    nombreSinAcentos = str.maketrans(_POSIBLE_VALOR_ENTRADA, _SALIDA)
    nombreSinAcentos = nombre.translate(nombreSinAcentos)
    nombreSinAcentos = nombreSinAcentos.title()
    return nombreSinAcentos


def existePais(pais):
    pais = convertirAcentosTitle(pais)
    if pais in ivaPaises:
        print(f'Valor del iva en {pais}--> {ivaPaises[pais]}')
        return True
    else:
        return False


def validarCantidad(cantidad):
    try:
        if cantidad > 0:
            cantidadIvaTotal = calcularIVA(cantidad)
            return True
        else:
            print('No es positivo el numero')
            return False
    except ValueError:
        return False


def calcularIVA(cantidad):
    print(cantidad)
    cantidadConIva = float(21 * cantidad)
    print(f'Importe a pagar: {cantidadConIva}')
    # return cantidadConIva


# Pedir País
pais = input('Escribe el pais para el que deseas saber el IVA: ')
while not existePais(pais):
    print('Debes introducir un pais de la Comunidad Economica Europea: ')
    # print(f'{ivaPaises.keys()}')
    pais = input('Escribe el pais para el que deseas saber el IVA: ')


# Introducir cantidad para pasar IVA
while True:
    try:
        cantidad = float(input('Introduce cantidad a aplicar IVA: '))
    except ValueError:
        print('Debes introducir una cantidad numérica y positiva. ')
    else:
        if not validarCantidad(cantidad):
            print('Debes introducir una cantidad numérica y positiva. ')
        else:
            break


ver = convertirAcentosTitle(pais)
# cantidadIvaTotal = calcularIVA(cantidad)

print(f'Nombre del pais --> {ver}')
