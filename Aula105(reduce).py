# reduce - faz a redução de um iterável em um valor
from functools import reduce

def funcao_reduce(acumulador, produto):
    return (acumulador + (produto['preco']))

produtos = [
    {'nome': 'Produto 5', 'preco': 10},
    {'nome': 'Produto 1', 'preco': 22},
    {'nome': 'Produto 3', 'preco': 2},
    {'nome': 'Produto 2', 'preco': 6},
    {'nome': 'Produto 4', 'preco': 4},
]

total = reduce(
    # funcao_reduce,
    lambda ac, p: ac + p['preco'],
    produtos,
    0
)

print(total)




# total = 0
# for p in produtos:
#     total += p['preco']

# print(round(total, 2))

# print(sum([p['preco'] for p in produtos]))