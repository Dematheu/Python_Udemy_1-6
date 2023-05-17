"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - Apaga o último item adicionado
update - Atualiza um dicionário com outro
"""
import copy

d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2],
    }
# d2 = d1.copy()
# # ou
# d2 = copy.copy(d1)
# # /\ ambos comandos são cópias rasas, então não copiam valores mutáveis, apenas replicam.
# # Ou seja, se mudar um lista dentro de uma variável dicionário, a cópia rasa faz com que todas essas listas mudem nas variáveis dicionários.
# d2['c1'] = 199
# d2['l1'][1] = 1000
# print(d1)
# print(d2)

'Para resolver isso temos o deep copy:'

d2 = copy.deepcopy(d1)

d2['c1'] = 199
d2['l1'][1] = 1000
print(d1)
print(d2)

# DEEP COPY VAI AFETAR TUDO NA LISTA, MUTÁVEL OU IMUTÁVEL



