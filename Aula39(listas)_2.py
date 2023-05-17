"""
Listas em Python
Tipo List - Mutável  ->  É MÚTAVEL PQ PODE SER ALTERADA
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append, insert, pop, del, clear, extend, +
Create, Read, Uptade, Delete = lista [i] (CRUD)

append: soma um item à lista

"""
lista = [10, 20, 30, 40]
# lista[2] = 300
# del lista[2] # quando deleta um indice da lista, os outros indices mudam de posição.
# print(lista)
# print(lista[2])
lista.append(50)
lista.append('str')
print(lista)

# lista.pop() # REMOVE O ÚTIMO ELEMENTO DA LISTA
ultimo_valor = lista.pop(3)
print(lista, 'removido', ultimo_valor)