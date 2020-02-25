import math

num = 0
for i in range(1, 1000000):
    num += (1/i**2)
print(num)

pi = math.sqrt(num*6)
print(f'El Numero pi es: {pi}')
