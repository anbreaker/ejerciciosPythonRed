# Crear un programa que reciba varias frases y que diga si cada una de ellas es un pangrama o no. 
# Sólo deberás considerar las letras del alfabeto en Español.
# La primera línea contendrá el número de frases y después aparecerá una nueva frase en cada línea. 
# Para cada frase deberás responder SI cuando se trate de un pangrama o NO cuando no lo sea.
#frase = 'El pingüino Wenceslao hizo kilómetros bajo exhaustiva lluvia y frio, añoraba a su querido cachorro'

listaDeFrases = []
contador = 0
numFrases = int(input('Nº Frases a entrar: '))

while(numFrases != contador):
    for i in range (numFrases):
        listaDeFrases.append(input("Introduzca la frase: "))
        contador += 1

def esPangrama(frase):
    alfabeto = "abcdefghijklmnñopqrstuüvwxyz"
    for letra in alfabeto: 
        if letra not in frase.lower(): 
            return False
    return True


for frase in listaDeFrases:
    if(esPangrama(frase) == True): 
        print("Es pangrama") 
    else: 
        print("No es pangrama") 

                
