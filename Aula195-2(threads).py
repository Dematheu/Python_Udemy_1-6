# Threads - Executando processamentos em paralelo
from threading import Lock, Thread
from time import sleep


class Ingressos:
    def __init__(self, estoque):
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()
        if self.estoque < quantidade:
            print('Acabou os ingressos.')
            self.lock.release()
            return

        sleep(1)

        self.estoque -= quantidade
        print(f'Você comprou {quantidade} ingresso(s).'
              f'Ainda temos {self.estoque} restantes.''\n')

        self.lock.release()


if __name__ == '__main__':
    ingressos = Ingressos(10)
    for i in range(1, 20):
        t = Thread(target=ingressos.comprar, args=(i,))
        t.start()

    print('', ingressos.estoque)
