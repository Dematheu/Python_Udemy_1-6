# Métodos em instâncias de classes Python
# O primeiro parâmetro é sempre 'self'
# Hard coded - É algo que foi escrito diretamente no código.

# Entendendo o self em classes:
# Classe - Molde (geralmente sem dados)
# Instância da classe (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando...')


fusca = Carro('Fusca')
# Carro.acelerar(fusca)
print(fusca.nome)
fusca.acelerar()

celta = Carro(nome='Celta')
print(celta.nome)
celta.acelerar()
