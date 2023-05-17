"""
Higher Order Functions -> Podem receber e/ou retornar outras funções
Frist-Class Functions -> Funções que são tratadas como outros tipos de dados comuns (strings, inteiros, etc..)
"""
def saudacao(msg, nome):
    return f'{msg}, {nome}'

def executa(funcao, *args):
    return funcao(*args)



print(
    executa(saudacao, 'Bom dia', 'Lucas')
)
print(
    executa(saudacao, 'Bom dia', 'Jonas')
)