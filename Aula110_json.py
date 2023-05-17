import json

'''---------------------CRIANDO ARQUIVO JSON--------------------'''

pessoa = {
    'nome': 'Lucas',
    'sobrenome': 'de Matheu',
    'enderecos': [
      {'rua': 'R1', 'num:': 30},
      {'rua': 'R2', 'num:': 65}
    ],
    'altura': 1.8,
    'numeros_preferidos:': (7, 14, 19, 27, 30),
    'dev': True,
    'nada': None,
}

with open('Aula110_json.json', 'w', encoding='utf8') as arquivo:
    json.dump(pessoa, arquivo, indent=2)

'''---------------------IMPORTANDO ARQUIVO JSON--------------------'''

with open('Aula110_json.json', 'r', encoding='utf8') as arquivo:
    pessoa = json.load(arquivo)
    print(pessoa)
    print(pessoa['nome'])