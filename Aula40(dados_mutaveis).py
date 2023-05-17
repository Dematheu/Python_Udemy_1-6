"""
Cuidado com dados mutáveis
= -> copiado o valor (imutáveis)
= -> aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Lucas', 'Roberta', 1, True]
lista_b = lista_a.copy() # para copiar o valor, e não apontar para o mesmo valor na memoria


lista_a[0] = 'Qualquer coisa'


print(lista_b)