# Relações entre classes: associação, agregação e composição
# Composição é uma especialização da agregação.
# Mas nela, quando o objeto "pai" for apagado, todas
# as referências dos objetos filhos também são
# apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) 
        # Garbage colector:
        # Quando a linguagem ver que não existe mais referência para determinado objeto
        # no programa, ela apaga o objeto da memória.
        # Neste exemplo: Todos os endereços serão apagados quando o Cliente for apagado,
        # já que a instância de endereço está sendo criada dentro da CLASSE CLIENTE

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco) 
        # Neste exemplo, ao criar um endereço sem referência ao objeto (Endereco()),
        # O objeto não está em composição com a classe, então ao apagar o Cliente,
        # Este endereço externo não será apagado.

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, ',', endereco.numero)
        
    def __del__(self):
        print('Apagando,', self.nome)

class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print('Apagando,', self.rua, self.numero)

cliente1 = Cliente('Maria')
cliente1.inserir_endereco('Av Brasil', 1500)
cliente1.inserir_endereco('Rua B', 56)
endereco_externo = Endereco('Avenida Saudade', 1221)
cliente1.inserir_endereco_externo(endereco_externo)
cliente1.listar_enderecos()

del cliente1

print(endereco_externo.rua, endereco_externo.numero)

print('***FIM DO CÓDIGO***')