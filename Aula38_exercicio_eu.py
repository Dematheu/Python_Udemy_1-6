"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.

for palavra_secreta in range(6):
    letra_escolhida = print('Escolha uma letra: ')
    letra = (next(iterador))

    if letra == letra_escolhida:

        print(letra)

"""

# palavra_secreta = 'abelha'
# tentativas = 0
# iterador = iter(palavra_secreta)
# letra = ''
# palavra_formatada = '******'
# i = 0

# print('Jogo da palavra secreta')

# while palavra_formatada != palavra_secreta:
#     letra_escolhida = input('Digite uma letra válida: ')
#     tamanho = (len(letra_escolhida))
#     apenas_letra = letra_escolhida
#     if tamanho > 1:
#         print('Digite apenas uma letra.')
#         continue
    
#     letra_valida = 'abelha'
#     if letra_escolhida != letra_valida:
#         tentativas += 1
#         continue

#     if letra_escolhida == letra_valida:
#         tentativas += 1
#         iterador(next) == letra_escolhida

import os

palavra_secreta = 'abelha'
tentativas = 0
iterador = iter(palavra_secreta)
letras_acertadas = ''
i = 0

while True:
    letra_escolhida = input('Digite uma letra válida: ')
    tamanho = (len(letra_escolhida))
    if tamanho > 1:
         print('Digite apenas uma letra.')
         continue
    tentativas += 1

    if letra_escolhida in palavra_secreta:
         letras_acertadas += letra_escolhida

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'
        os.system('cls')
    print('Palavra formada: ', palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print(f'Parabéns, a palavra é: {palavra_secreta}')
        break


print('Ao total foram', tentativas, 'tentativas')
tentativas = 0
letras_acertadas = ''
palavra_formada = ''
    
