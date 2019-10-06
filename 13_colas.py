# Colas FIFO

cola = ['Maria', 'Alejandro', 'Jose', 'Mario']

# Agregamos al final de la cola
cola.append('Carla')
cola.append('Flor')

print(cola)

# Sacando elementos pro el inicio de la cola FIFO (marcamos pop(0) con el indice 0)
n = cola.pop(0)
print(f'Sacando el primer elemento--> {n}')
n = cola.pop(0)
print(f'Sacando el primer elemento--> {n}')
print(cola)
