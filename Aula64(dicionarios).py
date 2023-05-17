# Dicionários em Python (tipo dict)
# Dicionários são estruturas de dados do tipo
# par de "chave" e "valor".
# Chaves podem ser consideradas como o "índice"
# que vimos na lista e podem ser de tipos imutáveis
# como: str, int, float, bool, tuple, etc.
# O valor pode ser de qualquer tipo, incluindo outro
# dicionário.
# Usamos as chaves - {} - ou a classe dict para criar
# dicionários.
# Imutáveis: str, int, float, bool, tuple
# Mutável: dict, list
# pessoa = {
#     'nome': 'Luiz Otávio',
#     'sobrenome': 'Miranda',
#     'idade': 18,
#     'altura': 1.8,
#     'endereços': [
#         {'rua': 'tal tal', 'número': 123},
#         {'rua': 'outra rua', 'número': 321},
#     ]
# }
# pessoa = dict(nome='Lucas', sobrenome='Parro de Matheu')

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'de Matheu',
    'idade': 31,
    'altura': 1.80,
    'endereços': [
        {'rua': 'Rua Uva Niágara', 'número': 663},
        {'rua': 'Av. Clotilde C. de Miranda', 'número': 220},
    ],
    'tipo sanguineo': 'A+',
}
# print(pessoa, type(pessoa))

print(pessoa['nome'], pessoa['sobrenome'])
print(pessoa['altura'])
print()

for chave in pessoa:
    print(chave, ':', pessoa[chave])