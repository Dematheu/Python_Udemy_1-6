"""
Introdução às funções (def) em Python.
Funções são trechos de código usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada)
"""
# def Print(a, b, c):
#     print('Várias')
#     print('Várias2')
#     print('Várias3')
#     print('Várias4')

# def imprimir(a, b, c): <- dentro dos parenteses são os parâmetros.
#     print(a, b, c)

# imprimir(1, 2, 3)  <- dentro dos parenteses são os argumentos.
# imprimir(4, 5, 6)
# imprimir(1, 2, 3)

def saudacao(nome='Sem nome'):
    print(f'Olá, {nome}')

saudacao('Mundo')
saudacao('José')
saudacao()