"""
Repetições
While (enquanto)
Executa uma ação enquanto uma condição for verdadeira.
Loop Infinito -> Quando um código não tem fim
"""
condicao = True

while condicao:
    nome = input('Qual seu nome: ')
    print(f'Seu nome é {nome}')

    if nome == 'sair':
        break  # Quebra o While mais próximo

print ('Acabou')