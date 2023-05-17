# Filter é um filtro funcional
# Pode ser feito através do list comprehension 
# Ou através de programação funcional

def print_iter(iterador):
    print(*list(iterador), sep='\n')
    print()

def filtrar_preco(p):
    return p['preco'] > 50

produtos = [
    {'nome': 'Produto 5', 'preco': 10.00},
    {'nome': 'Produto 1', 'preco': 22.32},
    {'nome': 'Produto 3', 'preco': 10.11},
    {'nome': 'Produto 2', 'preco': 105.87},
    {'nome': 'Produto 4', 'preco': 69.90},
]

# novos_produtos = [
#     p for p in produtos
#     if p['preco'] > 100
# ]

novos_produtos = filter(
    # lambda p: p['preco'] > 50,
    filtrar_preco,
    produtos
)

print_iter(produtos)
print_iter(novos_produtos)
