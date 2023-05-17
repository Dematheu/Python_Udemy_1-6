"""
enumerate - enumera iteráveis (índices)
"""
#[(0, 'Dema'), (1, 'Roberta'), (2, 'Maria'), (3, 'João')]     

lista =['Dema', 'Roberta', 'Maria']
lista.append('João')


for indice, nome in enumerate(lista):
    print(indice, nome)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, nome)

# for tupla_enumerada in enumerate(lista):
#     print('For da tupla: ')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')