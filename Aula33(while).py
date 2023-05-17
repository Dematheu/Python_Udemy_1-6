frase = 'O Python é uma linguagem de programação ' \
    'multiparadigma. ' \
    'Python foi criado por Guido van Rossum.'

i = 0
apareceu_mais = 0
letra_apareceu_mais = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qts_vzs_letra_apareceu_atual = frase.count(letra_atual)

    if apareceu_mais < qts_vzs_letra_apareceu_atual:
        apareceu_mais = qts_vzs_letra_apareceu_atual
        letra_apareceu_mais = letra_atual

    
    i += 1

print(
    'A letra que apareceu mais vezes foi:'
    f' "{letra_apareceu_mais}", que apareceu'
    f' {apareceu_mais} vezes.'
)