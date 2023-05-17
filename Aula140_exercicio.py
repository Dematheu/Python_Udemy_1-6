# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self, nome):
        self.nome = nome
        self._motor = None
        self._fabricante = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, valor):
        self._motor = valor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self, valor):
        self._fabricante = valor


class Motor:
    def __init__(self, nome):
        self.nome = nome

class Fabricante:
    def __init__(self, nome):
        self.nome = nome


car1 = Carro('Polo')
volks = Fabricante('VolksWagen')
car1.fabricante = volks
motor1000 = Motor('1.0')
car1.motor = motor1000
print(car1.nome, car1.fabricante.nome, car1.motor.nome)

car2 = Carro('C4 VTR')
citroen = Fabricante('Citroen')
car2.fabricante = citroen
motor2000 = Motor('2.0')
car2.motor = motor2000
print(car2.nome, car2.fabricante.nome, car2.motor.nome)

car3 = Carro('Jetta')
car3.fabricante = volks
car3.motor = motor2000
print(car3.nome, car3.fabricante.nome, car3.motor.nome)

car4 = Carro('Gol')
volks = Fabricante('VolksWagen')
car4.fabricante = volks
motor1000 = Motor('1.0')
car4.motor = motor1000
print(car4.nome, car4.fabricante.nome, car4.motor.nome)