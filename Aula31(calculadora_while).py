"""Calculadora com while"""

while True:
    num_1 = input('Digite um numero: ')
    num_2 = input('Digite outro: ')
    operador = input('Digite um operador [+][-][*][/]')

    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Um ou ambos os números não são válidos.')
        continue

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Calculando.....')
    if operador == '+':
        print(num_1_float + num_2_float)
    elif operador == '-':
        print(num_1_float - num_2_float)
    elif operador == '/':
        print(num_1_float / num_2_float)
    elif operador == '*':
        print(num_1_float * num_2_float)
    else:
        print('Não deveria chegar aqui.')

    sair = input('Quer sair? [s]im: ').lower().startswith('s')

    if sair:
        break
print('Fim')