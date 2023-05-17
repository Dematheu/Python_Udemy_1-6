"""
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
"""

# numero = input('Vou dobrar o numero que vc digitar: ')
# numero_float = float(numero)
# print(f'O dobro de {numero_float} é {numero_float * 2:.2f}')

numero_str = input('Vou dobrar o numero que você digitar: ')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')

except:
    print('Tá locão? Isso não é número!')

# if numero_str.isdigit():
#     numero_float = float(numero_str)
    # print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Tá locão? Isso não é número!')