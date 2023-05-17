"""
split e join com list e str
split - divide uma string
join - une uma string
"""

frase = '    Olha só que,    coisa interessante    '
lista_frases_crua = frase.split(',')

lista_frase = []

for i, frase in enumerate(lista_frases_crua):
    lista_frase.append(lista_frases_crua[i].strip())

# print(lista_frases_crua)
# print(lista_frase)

frases_unidas = ', '.join(lista_frase)
print(frases_unidas)