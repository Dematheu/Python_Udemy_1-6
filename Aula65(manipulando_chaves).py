# Manipulando chaves e valores em dicionários

pessoa = {}

chave = 'nome'

pessoa[chave] = 'Lucas' # Adiciona um valor ao dicionário 
pessoa['sobrenome'] = 'Parro'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])

