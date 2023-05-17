# Exercício com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou impar


resposta_par = 'O número escolhido é IMPAR'
resposta_impar = 'O número escolhido é PAR'
par_impar = True

def par_ou_impar():
    resultado = numero_escolhido % 2
    if resultado == 0:
        par_impar = False
        return par_impar
    par_impar = True
    return par_impar

while True:
    numero_escolhido = input('Digite um número inteiro: ')
    if numero_escolhido.isdigit():
        numero_escolhido = int(numero_escolhido)
        par_impar = par_ou_impar()
        break
    else:
        print('Favor digitar um número inteiro.')
        continue

if par_impar is True:
    print(resposta_par)
else:
    print(resposta_impar)
