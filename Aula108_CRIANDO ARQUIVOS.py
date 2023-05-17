import os
# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)
# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load
caminho_arquivo = 'C:\\Users\\Lucas\\Documents\\_PROGRAMACAO\\Python\\Udemy\\Atenção\\'
caminho_arquivo += 'aula108.txt'

# arquivo = open(caminho_arquivo, 'w')
...
# arquivo.close()

# with open(caminho_arquivo, 'w+') as arquivo:
#     arquivo.write('Ola mundo.\n')
#     arquivo.write('Hello world.\n')
#     arquivo.writelines(
#         ('Meu nome e Lucas\n', 'Muito prazer.')
#     )
#     arquivo.seek(0, 0)
#     # print(arquivo.read())
#     print('Lendo...')
#     arquivo.seek(0, 0)
#     print(arquivo.readline(), end='')
#     print(arquivo.readline().strip())
#     print(arquivo.readline().strip())
#     print('READLINES: ')
#     arquivo.seek(0, 0)
#     for linha in arquivo.readlines():
#         print(linha.strip())

# print('#' * 20)

# with open(caminho_arquivo, 'r') as arquivo:
#     print(arquivo.read())

with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Olá mundo.\n')
    arquivo.write('Hello world.\n')
    arquivo.writelines(
        ('Meu nome é Lucas\n', 'Muito prazer.')
    )

# os.remove(caminho_arquivo) ou unlink
# os.rename(caminho_arquivo, 'aula100-2.txt')