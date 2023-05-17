# Introdução às Generators functions em Python
# generator = (n for n in range(1000000))

# def generator(n=0, maximum=10):
#     yield 1    # Pausar
#     print('Continuando..')
#     yield 2    # Pausar
#     print('Mais uma vez..')
#     yield 3    # Pausar
#     print('Terminou')
#     return 'Acabou'

def generator(n=0, maximum=10):
    while True:
        yield n
        n += 1
        if n >= maximum:
            return
        



gen = generator(n=5, maximum=8)

for n in gen:
    print(n)