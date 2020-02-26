# Diccionarios

diccionario = {'azul': 'blue', 'rojo': 'red', 'verde': 'green'}

diccionario['amarillo'] = 'yellow'  # Agregar al diccionario.
diccionario['rojo'] = 'RED'  # Modificar al diccionario.
del(diccionario['verde'])  # Eliminar elementos

# print(diccionario)

agenda = {'Alejandro': {'edad': 22, 'estatura': 1.73},
          'Jose': [21, 1.75], 'Maria': [22, 1.67]}

# print(agenda['Alejandro'])

equipo = {10: 'Paulo Dybala', 11: 'Douglas Costa',
          7: 'Cristinao Ronaldo', 17: 'Mario Mandzukic'}

# Formas de mostrar la info de un diccionario:
print(f'El jugador con el numero 10 es --> {equipo[10]}')
# Evitando Keyerror si no existe dentro del diccionario la clave.
print(equipo.get(6, 'No agregue ese jugador'))
# Mostrar las "Claves" de un diccionario
print(f'Claves del diccionario "equipo"--> {equipo.keys()}')
# Mostrar los "Valores" de un diccionario
print(f'Valores del diccionario "equipo"--> {equipo.values()}')
# Recorrer diccionarios con items
print(equipo.items())
# Vaciar un diccionario .clear()
print(equipo.clear())

calificaciones = dict()

calificaciones['Algoritmos'] = 7
calificaciones['Matematicas'] = 8
calificaciones['Desarrolo web'] = 9
calificaciones['Bases de datos'] = 5

for key in calificaciones:
    print(f'Las claves del diccionarios son: {key}')

for key, value in calificaciones.items():
    print(f'Clave-> {key}     Valor-> {value}')

media = 0
for valor in calificaciones.values():
    media += valor / len(calificaciones.values())

print(media)