from threading import Thread
from time import sleep

# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self):
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThread('Hello World 01', 5)
# t1.start()
# t2 = MeuThread('Hello World 02', 15)
# t2.start()
# t3 = MeuThread('Hello World 03', 10)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)


# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=('Olá mundo 2!', 2))
# t2.start()

# t3 = Thread(target=vai_demorar, args=('Olá mundo 3!', 6))
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(.5)

def vai_demorar(texto, tempo):
    sleep(tempo)
    print(texto)


t1 = Thread(target=vai_demorar, args=('Olá mundo 1!', 10))
t1.start()
t1.join()

# while t1.is_alive():
#     print('esperando')
#     sleep(2)

print('acabou')
