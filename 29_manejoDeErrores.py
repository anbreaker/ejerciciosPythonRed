countries = {
    'España': 44,
    'Mejico': 122,
    'Colombia': 49,
    'Argentina': 43,
    'Chile': 18,
    'Perú': 31
}

while True:
    country = str(input('Escribe el nombre de un pais: ').lower().capitalize())
    
    try:
        print(f'La poblacion de {country} es de: {country, countries[country]} milloones')
    except KeyError:
        print(f'No tenemos el dato de poblacion del pais {country}')