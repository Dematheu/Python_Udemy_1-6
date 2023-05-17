# List comprehension em Python
# Lista comprehention é uma forma rápida para criar listas
# a partir de iteráveis.
# print(list(range(10)))
import pprint
def p(v):
    pprint.pprint(v, sort_dicts=False, width=40)

# lista = []
# for numero in range(10):
#     lista.append(numero)
# # print(lista)

# lista = [
#     numero * 2
#     for numero in range(10)
#     ]
# # print(lista)

# FILTRO DE DADOS EM LISTA COMPREHENSION
produtos = [
    {'nome': 'p1', 'preco': 20,},
    {'nome': 'p2', 'preco': 10,},
    {'nome': 'p3', 'preco': 30,},
]

novos_produtos = [
    {**produto, 'preco_novo': produto['preco'] * 1.05}   # MAPEAMENTO É QUANDO O IF VEM ANTES DO FOR
    if produto['preco'] > 20 else {**produto}            # FILTRO É QUANDO O IF VEM DEPOIS DO FOR
    for produto in produtos
    if produto['preco'] > 10
]
p(novos_produtos)