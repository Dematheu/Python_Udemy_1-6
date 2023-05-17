nome = 'Lucas de Matheu'
altura = 1.80
peso = 85
imc = peso / (altura * altura)  # tanto faz qual usar
imc = peso / altura ** 2       # tanto faz qual usar

print(nome, 'tem', altura, 'de altura,')
print('pesa', peso, 'quilos, e seu IMC é:')
print(imc)

# Lucas tem 1.80 de altura,
# pesa 85 quilos e seu IMC é
# 26.234567901234566

# podemos usar '...' como PLACEHOLDER
# ... é chamado Ellipsis
print(...)
