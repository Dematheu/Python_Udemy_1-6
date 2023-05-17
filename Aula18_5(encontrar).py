# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4
#  L u c a s
# -5-4-3-2-1

# nome = 'Lucas'
#print(nome[2])
#print(nome[-3])
# print('c' in nome)
# print('cas' in nome)
# print('z' in nome)
# print(10 * '-')
# print('c' not in nome)
# print('cas' not in nome)
# print('z' not in nome)

nome = input('Fala seu nome aí Jão: ')
encontrar = input('Que letra tu qué acha? ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não tá no {nome} não, comédia')