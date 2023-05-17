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

def listar(tarefas):
    print()
    if not tarefas:
        print('Nenhuma tarefa para listar')
        return
    print('Tarefas:')
    for tarefa in tarefas:
        print(f'\t{tarefa}')
#
def desfazer(tarefas, tarefas_refazer):
    print()
    if not tarefas:
        print('Nenhuma tarefa para desfazer')
        return
    tarefa = tarefas.pop()
    tarefas_refazer.append(tarefa)
#
def refazer(tarefas, tarefas_refazer):
    print()
    if not tarefas_refazer:
        print('Nenhuma tarefa para refazer')
        return
    tarefa = tarefas_refazer.pop()
    tarefas.append(tarefa)
#
def adicionar(tarefa, tarefas):
    print()
    tarefa = tarefa.strip()
    if not tarefa:
        print('Você não digitou nada.')
        return
    tarefas.append(tarefa)
#

tarefas = []
tarefas_refazer = []

while True:
    print('Comandos: listar, desfazer e refazer.')
    tarefa = input('Digite uma tarefa ou comando: ')

    if tarefa == 'listar':
        os.system('cls')
        listar(tarefas)
        continue
    elif tarefa == 'desfazer':
        desfazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'refazer':
        refazer(tarefas, tarefas_refazer)
        continue
    elif tarefa == 'clear':
        os.system('cls')

    elif tarefa == 'fim':
        os.system('cls')
        if tarefas == []:
            print('Sua lista está vazia.')
        else:
            print('Sua lista finalizada: ')
            n = 1
        for item in tarefas:
            print(f'{n}) {item}')
            n += 1
        break

    else:
        tarefas.append(tarefa)