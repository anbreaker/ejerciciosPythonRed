# Ejercicio 7
# Escribir un programa que pida al usuario su peso (en kg) y 
# estatura (en metros), calcule el índice de masa corporal y 
# lo almacene en una variable, y muestre por pantalla la frase 
# Tu índice de masa corporal es <imc> donde <imc> es el índice 
# de masa corporal calculado redondeado con dos decimales.
# IMC = Peso (kg) / altura (m)2

peso = int(input('¿Puede introducir su peso? '))
altura = int(input('¿Puede introducir su altura en cm '))

imc = (peso / ((altura/100)**2))

print('Tu índice de masa corporal es {:.2f} donde <imc> es el índice'.format(imc))
