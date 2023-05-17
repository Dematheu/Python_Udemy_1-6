"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""
from itertools import zip_longest

def somar_lista(l1, l2):
    intervalo = len(list(zip(l1, l2)))
    return [(l1[i] +l2[i]) for i in range(intervalo)]


l1 = [1, 2, 3, 40]
l2 = [10, 2, 3, 4, 5, 6, 7]

l_soma = somar_lista(l1, l2)

print('Solução minha: ')
print(l_soma)
print()
print('Outra Solução (professor): ')
l_soma2 = []
for i in range(len(l1)):
    l_soma2.append(l1[i] + l2[i])

print(l_soma2)

print()
print('Outra Solução (professor): ')  # mais 'Pythonica'
l_soma3 = []
for i, _ in enumerate(l1):
      l_soma3.append(l1[i] + l2[i])

print(l_soma3)

print()
print('Solução Preferencial pelo professor: ')  # mais 'Pythonica'
l_soma4 = [x + y for x, y in zip(l1, l2)]
print(l_soma4)


lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)]
print(lista_soma)  # [22, 4, 6, 10, 55, 60, 70]