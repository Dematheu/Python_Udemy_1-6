# Exercício - sistema de perguntas e respostas.
import os

contador_corretas = 0
numero_pergunta = 0
perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51', '61'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1', '10'],
        'Resposta': '5',
    },
]
print(perguntas[0].get('Opções'[3]))


print(perguntas[0].get('Pergunta'))

for opcao in perguntas[0].get('Opções'):
    print(numero_pergunta, ')', opcao)
    numero_pergunta += 1

resposta = input('Escolha uma opção: ')
if resposta == perguntas[0].get('Resposta'):
    print('Acertou!')
    contador_corretas += 1
else:
    print('Errou!')
print()

print(perguntas[1].get('Pergunta'))

numero_pergunta = 0
for opcao in perguntas[1].get('Opções'):
    print(numero_pergunta, ')', opcao)
    numero_pergunta += 1

resposta = input('Escolha uma opção: ')
if resposta == perguntas[1].get('Resposta'):
    print('Acertou!')
    contador_corretas += 1
else:
    print('Errou!')
print()

print(perguntas[2].get('Pergunta'))

numero_pergunta = 0
for opcao in perguntas[2].get('Opções'):
    print(numero_pergunta, ')', opcao)
    numero_pergunta += 1

resposta = input('Escolha uma opção: ')
if resposta == perguntas[2].get('Resposta'):
    print('Acertou!')
    contador_corretas += 1
else:
    print('Errou!')
print()

if contador_corretas == 3:
    print('Parabéns, você acertou todas as respostas.')
elif contador_corretas == 2:
    print('Quase lá. você errou uma resposta.')
elif contador_corretas == 1:
    print('Estude mais. Você acertou apenas uma respostas!')
else:
    print('Estude mais! Você errou todas as respostas!')






# print(12, 34, 1011, sep="-", end='##\n') # Adicionado o ##, se não tiver o \n não quebra a linha.
# print(56, 78, sep='-', end='\n')
# print(9, 10, sep='-', end='\n')

