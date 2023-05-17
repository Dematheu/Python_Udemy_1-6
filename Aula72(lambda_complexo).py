def executa(funcao, *args):
    return funcao(*args)

# def soma(x, y):
#     return x + y

# def cria_multiplicador(multiplicador):
#     def multiplica(numero):
#         return(numero * multiplicador)
#     return multiplica

# duplica = cria_multiplicador(2)
duplica = executa(
    lambda m: lambda n: n * m,
    2
)
print(duplica(3))

print(
    executa(
        lambda x, y: x + y,
        2, 3
    ),
    # executa(soma, 2, 3),
    # soma(2, 3)
)

print(
    executa(
        lambda *args: sum(args),
        1,4,3,5,4,4,5,3
    )
)