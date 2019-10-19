entrada = input('Probando entrada de Tildes ')

posibleValorEntrada = 'áéíóúüç'
salida = 'aeiouuz'
cambiarAcentos = str.maketrans(posibleValorEntrada, salida)
print(entrada.translate(cambiarAcentos))
