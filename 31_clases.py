class Bombilla:
    __BOMBILLA = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    def __init__(self, encendida):
        self.__encendida = True

    def encender(self):
        self.__encendida = True
        self.__interruptor()

    def apagar(self):
        self.__encendida = False
        self.__interruptor()

    def __interruptor(self):
        if self.__encendida:
            print(self.__BOMBILLA[0])
        else:
            print(self.__BOMBILLA[1])


def run():
    bombilla = Bombilla(encendida=False)

    while True:
        elegir = str(input('''
            ¿Qué deseas hacer?
            
            [E]ncender
            [A]pagar
            [S]alir
        '''))

        if elegir == 'e':
            bombilla.encender()
        elif elegir == 'a':
            bombilla.apagar()
        else:
            break


if __name__ == '__main__':
    run()
