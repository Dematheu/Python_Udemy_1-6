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
pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'de Matheu',
    'idade': 31
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])

# print(len(pessoa))
print(pessoa.keys()) # Podemos fazer a coerção para tuple ou lista, por exemplo
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))


# for items in pessoa.items():
#     print(items)

# for chave, valor in pessoa.items():
    # print(chave, valor)