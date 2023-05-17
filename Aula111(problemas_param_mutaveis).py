# Problema dos parâmetros mutáveis em funções Python

def adiciciona_clientes(nome, lista=None): # Não colocar a lista vazia como lista = [], pois seria um valor mutável
    if lista is None:                      # Em vez disso, trabalhar com o None, que é imutável, e tratar com 'if'
        lista = []
    lista.append(nome)
    return lista


cliente1 = adiciciona_clientes('Lucas')
adiciciona_clientes('Joana', cliente1)
adiciciona_clientes('Bruna', cliente1)
cliente1.append('Fernanda')
print(cliente1)

cliente2 = adiciciona_clientes('Helena')
adiciciona_clientes('Maria', cliente2)
adiciciona_clientes('Viviane', cliente2)
print(cliente2)

cliente3 = adiciciona_clientes('Jorge')
adiciciona_clientes('Robson', cliente3)
adiciciona_clientes('Stephany', cliente3)

print(cliente1)

print(cliente2)

print(cliente3)