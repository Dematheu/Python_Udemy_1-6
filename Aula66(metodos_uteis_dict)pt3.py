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

p1 = {
    'nome': 'Lucas',
    'sobrenome': 'de Matheu',
}
# print(p1.get('nome'))
# print(p1.get('idade')) # usando get, caso a chave não exista, ele retorna 'None', mas não dá erro
# print(p1.get('idade', 'Não existe')) # pode definir um retorno padrão para caso não exista.
# print()

# nome = p1.pop('nome') # Elimina a chave específicada, e retorna o valor
# print(nome)
# print(p1)

# ultima_chave = p1.popitem() # Elimina a última chave e retorna. Não pode especificar a chave, senão da erro.
# print(ultima_chave)
# print(p1)

# p1.update({ # CRIA OU MODIFICA VALORES.
#     'nome': 'novo valor',
#     'idade': 41,
# })

# p1.update(nome='novo valor', idade=30) # Outra forma de escrever
# print(p1)

tupla = ('nome', 'outro valor'), ('idade', 31) # Terceira forma de escrever. Se for passado apenas um valor na tupla, colocar virgula no final
lista = [['nome', 'outro valor'], ['idade', 31]] # Funciona com lista tambem;
p1.update(lista)
print(p1)