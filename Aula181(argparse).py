# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument(
    '-b', '--basic',
    help='Mostra "Olá mundo" na tela.',
    # type=str,
    metavar='STRING',
    # default='Olá mundo.',
    required=False,
    action='append',  # Recebe o argumento mais de uma vez
    # nargs='+' # Recebe mais de um valor
)

parser.add_argument(
    '-v', '--verbose',
    help='Mostra logs.',
    action='store_true'
)
args = parser.parse_args()
# print(args.b)

if args.basic is None:
    print('Você não passou o valor de B')
else:
    print(f'Valor de Basic: {args.basic}')

print(args.verbose)
