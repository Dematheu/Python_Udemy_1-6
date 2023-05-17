"""
Operadores de atribuição
= += -= *= /= //= **= %=
"""

contador = 0
while contador <= 10:
    contador += 1

    if contador >= 2 and contador <= 6:
        print('null')
        continue

    print(contador)

    if contador == 4:
        break

print("Acabou")