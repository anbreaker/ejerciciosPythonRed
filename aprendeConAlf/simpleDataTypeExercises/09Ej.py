# Ejercicio 9
# Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés anual y el número de años, y muestre por pantalla el capital 
# obtenido en la inversión.

cantidadInvertir = float(input("¿Cantidad a invertir? "))
interesAnual = float(input("¿Interés porcentual anual? "))
years = int(input("¿Años? "))
#round redondea al numero dedcimales que le pases al final
calculo = (round(cantidadInvertir * (interesAnual / 100 + 1) ** years, 3))
print("Capital final: {}".format(calculo))