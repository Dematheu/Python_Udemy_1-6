"""
for in com listas
0 Dema
1 Roberta
2 Maria
"""

lista =['Dema', 'Roberta', 'Maria']
lista.append('João')
indices = range(len(lista))

print(indices)

for indice in indices:
    print(indice, lista[indice])