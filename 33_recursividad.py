# 1- Sacar la suma de 1 al numero dado. Ej: 5, devuelve 5+4+3+2+1 = 15
# 2- Sacar el factorial de un numero
# 3- recorrer una lista de froma recursiva


def suma_recursiva(numero):
    if numero == 1:
        return 1
    else:
        operacion = numero + suma_recursiva(numero - 1)
        return operacion


def factorial(numero):
    if numero == 1:
        return 1
    else:
        return numero * factorial(numero - 1)
    
lista = ['elemento1', 'elemento2', 'elemento3', 'elemento4', 'elemento5']

def mostrar_lista_recursivamente(lista, index):
    if index != len(lista):
        print(lista[index])
        mostrar_lista_recursivamente(lista, index + 1)


print(suma_recursiva(5))
print(factorial(5))
print(mostrar_lista_recursivamente(lista, 0))