"""While / Else"""

string = "Valor qualquer"

i = 0
while i < len(string):
    letra = string[i]

    if letra == 'z':
        break

    print(letra)
    i += 1
else:
    print('Não há letra z na string')
print('Fora do while.')