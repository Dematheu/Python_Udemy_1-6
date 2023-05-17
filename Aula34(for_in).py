"""For / In :  ESTRUTURA DE REPETIÇÃO PARA COISAS FINITAS"""

texto = 'Python'
novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
print(novo_texto + '*')