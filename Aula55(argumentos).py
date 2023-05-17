"""
Argumentos nomeados e nao nomeados em funções Python
Argumento nomeado tem nome com sinal de igual =
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z = ', x + y + z)

soma(1, 2, 3)        # Esses são os argumentos não nomeados (ou posicionais). Os parametros recebem os argumentos na ordem indicada.
soma(y=2, z=3, x=1)  # Esses são os argumentos nomeados. Eu indico nos parenteses qual parametro recebe qual argumento.

soma(1, 2, z=5)      # Pode haver argumentos nomeados e não nomeados juntos, porém, a partir do primeiro argumento nomeado, 
                     #todos na sequencia devem ser nomeados tbm. Geralmente não se mistura, apenas em grande necessidade.

