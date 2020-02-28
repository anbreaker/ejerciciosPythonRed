# Decoradores en Python
# Un decorador es una función que recibe otra función y regresa una tercera función.
# Para reconocer un decorador, puedes ver que tienes un arroba sobre la declaración de una función.


def protegida(func):
    def wrapper(password):
        if password == 'pass':
            return func()
        else:
            print('Contraseña Incorrecta')

    # Devolvemos el objeto y no queremos devolver la nueva ejecucion del metodo.
    return wrapper


@protegida
def funcion_protegida():
    print('Contraseña Correcta')


# 2º Ejemplo
# A, B, C son funciones
# A recibe como parametro B para poder crear C

def decorador(es_valido=True):
    def decorador2(func):
        def antes_accion():
            print('Se va a ejecutar la funcion')

        def despues_accion():
            print('Se ejecutó la funcion')

        def nueva_funcion(*args, **kwargs):
            if es_valido:
                antes_accion()

            resultado = func(*args, **kwargs)
            despues_accion()

            return resultado
        return nueva_funcion
    return decorador2


@decorador(es_valido=True)
def suma(num1, num2):
    return num1 + num2


resultado = suma(2, 3)
print(resultado)


if __name__ == "__main__":
    password = str(input('Ingresa tu contraseña: '))

    funcion_protegida(password)
