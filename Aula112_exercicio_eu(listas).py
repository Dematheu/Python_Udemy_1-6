# Exercício - Lista de tarefas com desfazer e refazer

# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
import os
import sys
todo = []
refazer = []
desfazer = []


while True:
    print('Comandos: listar, desfazer, refazer')
    escolha = input('Digite uma tarefa ou comando: ')
    print()

    if escolha == 'listar':
        os.system('cls')
        if todo == []:
            print('Sua lista está vazia.')
        else:
            print('LISTA DE TAREFAS: ')
            n = 1
            for item in todo:
                print(f'{n}) {item}')
                n += 1

    elif escolha == 'desfazer':
        if todo == []:
            print('Nada a desfazer.')
            print()
        else:
            adic = todo.pop()
            refazer.append(adic)

    elif escolha == 'refazer':
        if refazer == []:
            print('Nada a refazer')
            print()
        else:
            adic = refazer.pop()
            todo.append(adic)

    elif escolha == 'clear':
        os.system('cls')

    elif escolha == 'fim':
        os.system('cls')
        if todo == []:
            print('Sua lista está vazia.')
        else:
            print('Sua lista finalizada: ')
            n = 1
        for item in todo:
            print(f'{n}) {item}')
            n += 1
        break

    else:
        todo.append(escolha)