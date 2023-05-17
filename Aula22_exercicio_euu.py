"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é:
        Seu nome invertido é:
        Se nome contem (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios"
"""
nome = input('Digite o seu nome: ')
idade = input('Digite a sua idade: ')
encontrar = ' '
'numero_letras'


if not nome:
    print(f'Desculpe, você deixou compos vazios.')
elif not idade:
    print(f'Desculpe, você deixou compos vazios.')
else:
    print(f'Seu nome é: {nome}.')
    print(f'Você tem {idade} anos.')
    print('Seu nome ao contrário é: ', nome[::-1])
    if encontrar in nome:
        print('Seu nome contém espaço.')
    else:
        print('Seu nome NÃO contém espaço.')
    print('Seu nome tem XX letras')
    print('A última letra do seu nome é : ', nome[::-1])

    # não consegui 100%