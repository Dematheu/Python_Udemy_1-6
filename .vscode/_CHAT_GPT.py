produtos = {
    1: {'nome': 'Camiseta', 'preco': 29.90},
    2: {'nome': 'Calça', 'preco': 59.90},
    3: {'nome': 'Tênis', 'preco': 99.90},
    4: {'nome': 'Bermuda', 'preco': 39.90},
    5: {'nome': 'Jaqueta', 'preco': 149.90},
    6: {'nome': 'Blusa', 'preco': 49.90},
    7: {'nome': 'Shorts', 'preco': 29.90},
    8: {'nome': 'Chinelo', 'preco': 19.90},
    9: {'nome': 'Vestido', 'preco': 79.90},
    10: {'nome': 'Saia', 'preco': 39.90},
    11: {'nome': 'Sapato', 'preco': 129.90},
    12: {'nome': 'Sandália', 'preco': 89.90},
    13: {'nome': 'Óculos', 'preco': 59.90},
    14: {'nome': 'Relógio', 'preco': 99.90},
    15: {'nome': 'Boné', 'preco': 19.90}
}

carrinho = []

def adicionar_produto():
    id_produto = int(input('Digite o id do produto: '))
    quantidade = int(input('Digite a quantidade: '))
    
    produto = produtos.get(id_produto)
    if produto:
        produto_no_carrinho = False
        for item in carrinho:
            if item['produto']['id'] == id_produto:
                item['quantidade'] += quantidade
                produto_no_carrinho = True
                break
        if not produto_no_carrinho:
            carrinho.append({'produto': produto, 'quantidade': quantidade})
        print('Produto adicionado ao carrinho com sucesso!')
    else:
        print('Produto não encontrado!')

def remover_produto():
    id_produto = int(input('Digite o id do produto: '))
    
    produto_no_carrinho = False
    for item in carrinho:
        if item['produto']['id'] == id_produto:
            carrinho.remove(item)
            produto_no_carrinho = True
            break
    if produto_no_carrinho:
        print('Produto removido do carrinho com sucesso!')
    else:
        print('Produto não encontrado no carrinho!')

def listar_carrinho():
    total = 0
    print('Produtos no carrinho:')
    for item in carrinho:
        produto = item['produto']
        quantidade = item['quantidade']
        preco = produto['preco']
        subtotal = preco * quantidade
        total += subtotal
        print(f"{produto['nome']} - {quantidade} x R${preco:.2f} = R${subtotal:.2f}")
    print(f'Total: R${total:.2f}')

while True:
    print('Escolha uma opção:')
    print('1 - Adicionar produto')
    print('2 - Remover produto')
    print('3 - Listar carrinho')
    print('4 - Sair')
    opcao = int(input())
    if opcao == 1:
        adicionar_produto()
    elif opcao == 2:
        remover_produto()
    elif opcao == 3:
        listar_carrinho()
    elif opcao == 4:
        print('Obrigado')
    else:
        break
