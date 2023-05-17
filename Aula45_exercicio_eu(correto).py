"""
EXERCICIO:
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com
erros de índices inexistentes na lista
"""

import os
lista = []
condicao = True


while condicao:    
    opcao = input(
        'Selecione uma opção: ' 
        '[i]nserir [a]pagar [l]istar [f]inalizar: '
        )

    if opcao == 'i' or opcao == 'I':
        item = input('Qual item deseja adicionar? ')
        lista.append(item)

    elif opcao == 'a' or opcao == 'A':
        item_apagar = input('Qual item deseja apagar? ')
        if item_apagar.isdigit():
            indice = int(item_apagar)
            if indice <= len(lista):
                del lista[indice]

    elif opcao == 'l' or opcao == 'L':
        os.system('cls')
        if len(lista) == 0:
            print('Sua lista está vazia.')
        
        elif len(lista) > 0:
            print('Sua lista atual: ')
        for indice, nome in enumerate(lista):
            print(indice, '-', nome)

    elif opcao == 'f' or opcao == 'F':
        break

    else:
        print('Digite uma opão válida: ')

os.system('cls')
if len(lista) == 0:
    print('Sua lista está vazia.')
else:
    print('Sua lista finalizada: ')
for indice, nome in enumerate(lista):
    print(indice, '-', nome)