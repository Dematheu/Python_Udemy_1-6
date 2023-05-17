"""
Iterável -> str, range, etc (__iter__)
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador
Método é basicamente o que vem depois do '.' ponto. Uma ação dentro do objeto.
"""

# texto = (iter('Lucas'))   __iter__()
# print(next(texto))        __next__()

# texto = 'Lucas'        # iterável
# iterador = iter(texto)# iterador

# while True:
#     try:
#         print(next(iterador))
#     except StopIteration:
#         break