import json
CAMINHO_ARQUIVO = 'Aula122_json.json'

class Cars:
    def __init__(self, brand, name, color, year):
        self.brand = brand
        self.name = name
        self.color = color
        self.year = year



car1 = Cars('Volkswagen', 'Fusca', 'vermelho', 1975)
car2 = Cars('Citroen', 'C4 VTR', 'preto', 2006)
car3 = Cars('GM', 'Onix', 'prata', 2020)
cl = [vars(car1), vars(car2), vars(car3)]

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

def fazer_dump():
    with open(CAMINHO_ARQUIVO, 'w', encoding='utf8') as arquivo:
        print('Fazendo Dump')
        json.dump(cl, arquivo, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    print('Arquivo Main')
    fazer_dump()