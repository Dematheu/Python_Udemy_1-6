"""
Exervcícios
Crie funções que duplicam, triplicam e quadriplicam
o número recebido como parâmetro
"""

def multiplicar(numero):
    def multi(multiplicador):
        return (numero * multiplicador)
    return multi

numero_escolhido = int(input('Digite um número: '))
multi_escolhido = int(input('Escolha um multiplicador: '))
numero = multiplicar(numero_escolhido)
# multiplicador_escolhido = input('Digite um multiplicador: ')

print(numero(multi_escolhido))

# for multiplicador in range(multi_escolhido):
#     print(numero(multiplicador))


    # resultado = multiplicar(numero_escolhido)
    # print(resultado)
