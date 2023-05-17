# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

def parametros_decorador(a):
    def decorador(func):
        print(a)
        def interna(*args, **kwargs):
            l_int = (l1[a] + l2[a])
            print(f'{a}, {l_int}')
            return l_int
        return interna
    return decorador

@parametros_decorador(2)
@parametros_decorador(1)
@parametros_decorador(0)
def juntar_listas(x, y):
    return x + y

l1 = ['Salvador', 'Ubatuba', 'Belo Horizonte']
l2 = ['BA', 'SP', 'MG', 'RJ']
lc = juntar_listas(l1, l2)

print(lc)