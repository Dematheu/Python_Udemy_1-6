# Combinations, Permutations, e Product - Itertools
# Combinations: Ordem não importa - Iterável + tamanho do grupo
# Permutação: Ordem importa
# Produto: Ordem Importa e repete valores únicos
from itertools import combinations, permutations, product

def print_iter(iterator):
    print(*list(iterator), sep='\n')
    print()

pessoas = [
    'Livia', 'Joana', 'Lucas', 'Mariana'
]
camisetas = [
    ['preta', 'branca'],
    ['p', 'm', 'g'],
    ['masculino', 'feminino', 'unisex'],
    ['algodão', 'poliester'],
]

# print_iter(combinations(pessoas, 2))
# print_iter(permutations(pessoas, 2))
print_iter(product(*camisetas))