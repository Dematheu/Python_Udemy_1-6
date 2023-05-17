"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.
Conta (ABC)
    ContaCorrente
    ContaPoupanca
Pessoa (ABC)
    Cliente
        Clente -> Conta
Banco
    Banco -> Cliente
    Banco -> Conta
Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abstractmethod
    def _sacar(self, valor):
        if valor > self:
            print('Saldo insuficiente')
        return self - valor


class ContaCorrente(Conta):
    def criar_conta(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    def _sacar(self, saldo, valor):
        if valor > saldo:
            print('Saldo insuficiente')
        return self.saldo - valor


class ContaPoupanca(Conta):
    def criar_conta(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo
        return

    def _sacar(self, saldo, valor):
        if valor > saldo:
            print('Saldo insuficiente')
        return self.saldo - valor


class Pessoa(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        self._nome = valor

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, valor):
        self._idade = valor


class Cliente(Pessoa, Conta):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    # def cliente_completo():
    #     for indice in Cliente:
    #         ...


class Banco(Cliente, Conta):
    ...


c1 = Pessoa('Lucas', 31)
c2 = Pessoa('Maria', 26)
c3 = Pessoa('Ana', 28)

# cc1 = ContaCorrente('001', 1001, 9000)
# print(
#     cc1.__class__.__name__, ':\n'
#     'Agência:', cc1.agencia, '\n'
#     'Número da conta:', cc1.numero, '\n'
#     'Saldo:', cc1.saldo, '\n'
#     )

# cc2 = ContaCorrente('002', 2002, 85000)
# print(
#     cc2.__class__.__name__, ':\n'
#     'Agência:', cc2.agencia, '\n'
#     'Número da conta:', cc2.numero, '\n'
#     'Saldo:', cc2.saldo, '\n'
#     )

# cc3 = ContaPoupanca('003', 3003, 500)
# print(
#     cc3.__class__.__name__, ':\n'
#     'Agência:', cc3.agencia, '\n'
#     'Número da conta:', cc3.numero, '\n'
#     'Saldo:', cc3.saldo, '\n'
#     )

# cc2._sacar(cc2.saldo, 400)
# print(cc2.saldo)

# cc4 = ContaPoupanca.criar_conta(cc1, '001', 4004, 9950)
# print(cc4)
