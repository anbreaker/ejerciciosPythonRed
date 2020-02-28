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

    def __init__(self, _encendida):
        self._encendida = True

    def encender(self):
        self._encendida = True
        self._interruptor()

    def apagar(self):
        self._encendida = False
        self._interruptor()

    def _interruptor(self):
        if self._encendida:
            print(self.__BOMBILLA[0])
        else:
            print(self.__BOMBILLA[1])


def run():
    bombilla = Bombilla(_encendida=False)

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
