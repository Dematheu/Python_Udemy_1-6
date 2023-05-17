nome = 'Lucas de Matheu'
altura = 1.80
peso = 85
imc = peso / (altura * altura) # tanto faz qual usar
imc = peso / altura ** 2       # tanto faz qual usar

"f-strings"
linha_1 = f'{nome} tem {altura:.2f} de altura' # f no começo de string habilita usar variáveis dentro do texto
                                               # colocar { colchetes } para adicionar as variáveis
                                               # .2f após a variavel determina nº de casas decimais
linha_2 = f'pesa {peso} quilos, e seu IMC é:'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)

# Lucas tem 1.80 de altura,
# pesa 85 quilos e seu IMC é
# 26.234567901234566

# podemos usar '...' como PLACEHOLDER
# ... é chamado Ellipsis
print(...)