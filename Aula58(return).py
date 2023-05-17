"""
Retorno de valores das funções (return)
"""
def soma(x, y):
    if x > 10:
        return [10, 20]
    return x + y
    print(1 + 1)   # Após o return, a função se encerra. (Funciona parecido com um break)

# variavel = soma(1, 2)
# variavel = int('1')
soma1 = soma(2, 2)
soma2 = soma(3, 3)

print(soma(9, 10))
print(soma(11, 44))


print(f'{soma1=} + {soma2=} = {soma1 + soma2}')