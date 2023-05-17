"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO
multiplicando cada um dos valores por uma
contagem regressiva começando de 11

Ex.:  746.824.890-70 (746824890)
   11  10 9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7  <--- PRIMEIRO DIGITO
   77  40 54 64 14 24 40 36 0  14
Somar todos os resultados: 
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O primeiro dígito do CPF é 7
"""

cpf = '74682489070'
indices = range(len(cpf)) # indices poderia sertmbém um fatiamento. ex: indices = cpf[:9]
soma_cpf = 0
numero_atual = 0
fator_mult = 10
contagem = 0

# for indice in indices:
#     if contagem > 8:
#         break
#     if cpf[indice].isdigit:
#         numero_atual = int(cpf[indice])
#         soma_cpf += (numero_atual) * (fator_mult)
#         fator_mult -= 1
#         contagem += 1
#     else:
#         break

# print('Soma 9 valores:', soma_cpf)
# print('A soma dos 9 primeiros digitos do CPF '
#     'multiplicando cada um dos valores por uma '
#     'contagem regressiva começando de 10 é:', soma_cpf)
# print('')

# digito_1 = (soma_cpf * 10) % 11

# print('Primeiro digito do CPF:')
# print(digito_1 if digito_1 < 10 else 0)

soma_cpf = 0
fator_mult = 11
contagem = 0

for indice in indices:
    if contagem > 9:
        break
    if cpf[indice].isdigit:
        numero_atual = int(cpf[indice])
        soma_cpf += (numero_atual) * (fator_mult)
        fator_mult -= 1
        contagem += 1
    else:
        break

print('Soma 10 valores:', soma_cpf)
digito_2 = (soma_cpf * 10) % 11
print('Segundo digito do CPF:')
print(digito_2 if digito_2 < 10 else 0)