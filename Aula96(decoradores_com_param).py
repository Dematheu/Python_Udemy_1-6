# Decoradores com parâmetros

def fabrica_de_decoradores(a=None, b=None, c=None):     # Primeira função: pegar os parâmetros do decorador.
    def fabrica_de_funcoes(func):                       # Segunda função: para pegar a função. É o decorador.
        print('Decoradora 1: ')

        def aninhada(*args, **kwargs):                  # Terceira função: É a função que será executada.
            print('Parâmetros do decorador: ', a, b, c)
            print('Aninhada: ')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes



@fabrica_de_decoradores(1, 2, 3)
def soma(*args):
    return sum(args)

# def multiplica(x,y):
#     return x * y

decoradora = fabrica_de_decoradores()
multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

dez_mais_cinco = soma (10)
dez_vezes_cinco = multiplica(10, 5)
print(dez_mais_cinco)
print(dez_vezes_cinco)
