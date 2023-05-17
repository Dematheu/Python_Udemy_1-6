# O que é json? JAVA SCRIPT OBJECT NOTATION
# Basicamente uma estrutura de dados que foi criada para que você transporte ou salve dados.

# Posso ter alguns tipos de dados:
# Boolean;
# Numero (inteiro ou floar);
# Null;
# String;
# [lista ou array];
# {Dicionário} - *** Usar aspas duplas na chave, e no valor caso seja string ***

# Pode ter apenas um dado.

# A estrutura de dados json é muito simples. Ela não suporta coisas que executam ações específicas
# EX: funções, métodos, classes, sets. Não consegue jogar isso num json.

# Se uma TUPLA ou LISTA for enviada do Python pro JSON, ela vira um array.
# Se um ARRAY for enviado do JSON pro Python, ele vira uma lista.
# Então se a tupla for necessária, tem que se atentar nisso.

import json
import os

# pessoas = [
#     {
#         "nome": "Lucas",
#         "sobrenome": "de Matheu",
#         "idade": 31,
#         "ativo": False,
#         "notas": [
#             "A",
#             "A+"
#         ],
#         "telefones": {
#             "comercial": "11 99999-9999",
#             "pessoal": "11 98888-8888"
#         }
#     },
#     {
#         "nome": "Roberta",
#         "sobrenome": "D'Ambrosio",
#         "idade": 30,
#         "ativo": False,
#         "notas": [
#             "A+",
#             "B"
#         ],
#         "telefones": {
#             "comercial": "11 97777-7777",
#             "pessoal": "11 94444-5555"
#         }
#     }
# ]

# BASE_DIR = os.path.dirname(__file__)
# SAVE_TO = os.path.join(BASE_DIR, 'Aula109_arquivo-python.json')

# with open(SAVE_TO, 'w') as file:
#     json.dump(pessoas, file, indent=2)

# print(json.dumps(pessoas, indent=2))

# BASE_DIR = os.path.dirname(__file__)
# JSON_FILE = os.path.join(BASE_DIR, 'Aula109_arquivo-python.json')

# with open(JSON_FILE, 'r') as file:
#     pessoas = json.load(file)
#     print(json.dumps(pessoas))
    
    # for pessoa in pessoas:
    #     print(pessoa['nome'])

json_string = '''
[{"nome": "Lucas", "sobrenome": "de Matheu", "idade": 31, "ativo": false, "notas": ["A", "A+"], "telefones": {"comercial": "11 99999-9999", "pessoal": "11 98888-8888"}}, {"nome": "Roberta", "sobrenome": "D'Ambrosio", "idade": 30, "ativo": false, "notas": ["A+", "B"], "telefones": {"comercial": "11 97777-7777", "pessoal": "11 94444-5555"}}]
'''

pessoas = json.loads(json_string)

for pessoa in pessoas:
    print(pessoa['nome'])