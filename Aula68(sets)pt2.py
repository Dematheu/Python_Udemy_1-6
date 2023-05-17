# Sets - Conjuntos em Python (tipo set)
# Conjuntos são ensinados na matemática
# https://brasilescola.uol.com.br/matematica/conjunto.htm
# Representados graficamente pelo diagrama de Venn
# Sets em Python são mutáveis, porém aceitam apenas
# tipos imutáveis como valor interno.

# Criando um set
# set(iterável) ou {1, 2, 3}

# s1 = set('Lucas')
# s2 = set() # set vazio
# s1 = {'Lucas', 1, 2, 3} # set com dados
# print(s1, type(s1), type(s2))

'-------------'

# Sets são eficientes para remover valores duplicados
# de iteráveis.
# - Não aceitam valores mutáveis;
# - Seus valores serão sempre únicos;
# - não tem índexes;
# - não garantem ordem;
# - são iteráveis (for, in, not in)

# l1 = [1, 2, 3, 4, 5, 6, 6, 8, 9, 9, 9, 9, 9, 9]
# s1 = set(l1)
# l2 = list(s1)
# # s1 = {1, 2, 3, 3, 3, 3, 3, 3, 2, 2, 1}
# s1 = {1, 2, 3, 4, 5, 6, 7, 8}
# print(3 in s1)
# for numero in s1:
#     print(numero)

# Métodos úteis:
# add, update, clear, discard

# s1 = set()
# s1.add('Lucas')
# s1.add(1)
# s1.update(('Olá mundo', 1, 2, 3, 4))
# # s1.clear()  # Limpa o set
# s1.discard('Olá mundo')
# print(s1)

# Operadores úteis:
# união | união (union) - Une
# intersecção & (intersection) - Itens presentes em ambos
# diferença - Itens presentes apenas no set da esquerda
# diferença simétrica ^ - Itens que não estão em ambos

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2  # união
print('UNIÃO:',s3)
s3 = s1 & s2  # intersecção
print()
print('INTERSECÇÃO:',s3)
s3 = s1 - s2  # diferença (UNICO ONDE A ORDEM IMPORTA!!!)
print()
print('DIFERENÇA:', s3)
s3 = s1 ^ s2  # diferença simétrica
print()
print('DIFERENÇA SIMÉTRICA:', s3)
