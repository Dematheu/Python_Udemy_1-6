# map - para mapear dados
# Mapeamento é uma função que faz como o list comprehension, 
# mas através de uma função no primeiro parametro, 
# e um iteravel no segundo parametro

from functools import partial
from types import GeneratorType

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()


produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

def aumentar_porcentagem(valor, porcentagem):
    return round(valor * porcentagem, 2)

aumentar_dez_pct = partial(
    aumentar_porcentagem,
    porcentagem=1.1
)

# novos_produtos =[
#     {**p, 'preco': aumentar_dez_pct(p['preco'])} for p in produtos
# ]
def muda_preco_produtos(produto):
    return {**produto, 
            'preco': aumentar_dez_pct(produto['preco'])}

novos_produtos = list(map(
    muda_preco_produtos,
    produtos)
)



print_iter(produtos)
print_iter(novos_produtos)

print(novos_produtos)
print(hasattr(novos_produtos, '__iter__'))
print(hasattr(novos_produtos, '__next__'))


# novos_produtos = (x for x in produtos)
# print(isinstance(novos_produtos, GeneratorType))

print(
    list(map(
        lambda x: x * 3,
        [    1, 2, 3, 4]
    )
))