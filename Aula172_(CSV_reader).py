# csv.reader e csv.DictReader
# csv.reader lê o CSV em formato de lista
# csv.DictReader lê o CSV em formato de dicionário
import csv
from pathlib import Path

CAMINHO_CSV = Path(__file__).parent / 'Aula172-ex.csv'


# with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
#     reader = csv.reader(arquivo)

#     for line in reader:
#         print(line)

with open(CAMINHO_CSV, 'r', encoding='utf8') as arquivo:
    reader = csv.DictReader(arquivo)

    for line in reader:
        print(line['Nome'], line['Idade'], line['Endereço'])
