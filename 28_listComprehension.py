# List comprehension

pares = []

for num in range (1,31):
    if num % 2 == 0:
        pares.append(num)

# Ejemplo con List comprehension

even = [num for num in range(1,31) if num % 2 == 0]

print(f'Representacion tradicional lista {pares} \nRepresentacion con list comprehension {even}')


# Dicionarios comprehension

cuadrados = {}
for num in range(1,11):
    cuadrados[num] = num**2
    
        # clarve:  valor
squares = {num: num**2 for num in range(1,11)} 

print(f'Representacion tradicional lista {cuadrados} \nRepresentacion con list comprehension {squares}')
