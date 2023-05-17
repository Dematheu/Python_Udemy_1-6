# Exercício com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável

# Crie uma função que fala se um número é par ou ímpar.
# Retorne se o número é par ou impar

numero_adicional = None

def multiplicador(*args):
    resultado = 1
    for numero in args:
        resultado *= numero
    return resultado
    
def adicionar():
    numero_adicional = input('Digite um número inteiro: ')
    if numero_adicional.isdigit():
        return numero_adicional
    else:
        adicionar()

resultado = 0

while True:
    numero_escolhido_1 = input('Digite um número inteiro: ')
    numero_escolhido_2 = input('Digite outro número inteiro: ')
    if numero_escolhido_1.isdigit() and numero_escolhido_2.isdigit():
        numeros_escolhidos = int(numero_escolhido_1), int(numero_escolhido_2)
    else:
        print('Você não digitou números inteiros.')
        continue
    break

while True:
    adicionar_mais = input('Deseja adicionar mais números? [s]')
    if adicionar_mais == 's':
        numero_adicional = int(adicionar())
        numero_adicional_int = [numero_adicional]
        numero_adicional_int = tuple(numero_adicional_int)
        numeros_escolhidos = (numeros_escolhidos + numero_adicional_int)
    else:
        break

print(f'(A multiplicação de {numeros_escolhidos} é: ')    
resultado = multiplicador(*numeros_escolhidos)
print('O resultador da multiplicação é:', resultado)