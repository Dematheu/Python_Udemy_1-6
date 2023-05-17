"""
Iterando strings com while
"""
#       012345678910
nome = 'Smitty Webber Jeager Menjensen'  #Strings são iteráveis
contador = 0
novo_nome = ''
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)
novo_nome += '*'
while contador < tamanho_nome:
    letra = nome[contador]
    novo_nome += f'*{letra}'
    print(novo_nome)
    contador += 1
novo_nome += '*'
print(novo_nome)