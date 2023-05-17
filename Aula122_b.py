import json
import os
from Aula122_a import CAMINHO_ARQUIVO, Cars

with open(CAMINHO_ARQUIVO, 'r') as arquivo:
    cl = json.load(arquivo)
    car1 = Cars(**cl[0])
    car2 = Cars(**cl[1])
    car3 = Cars(**cl[2])

# os.system('cls')
print(f'CARRO 1: \nMarca: {car1.brand} \nModelo: {car1.name} \nCor: {car1.color} \nAno: {car1.year}\n')
print(f'CARRO 2: \nMarca: {car2.brand} \nModelo: {car2.name} \nCor: {car2.color} \nAno: {car2.year}\n')
print(f'CARRO 3: \nMarca: {car3.brand} \nModelo: {car3.name} \nCor: {car3.color} \nAno: {car3.year}')
