print(12, 34) # Utilizada para exibir as coisas na tela. Recebe o que chamamos de 'ARGUMENTO'.
#Utilizar Ctrl+C e Ctrl+V copia a linha inteira
print(56, 78)

# \r\n -> CRLF: Significa RETURN e LINE FEED, respectivamente, e faz com que quebre a linha, no Windows são caracteres que nós não vemos. (No MAC e no Linux é visível)
# \n -> LF
print(12, 34, 1011, sep="-") # Adicionado o comando 'SEPARADOR', determina o espaço entre os ARGUMENTOS.
print(56, 78, sep='-')
print(9, 10, sep='-')


print(12, 34, 1011, sep="-", end='##\n') # Adicionado o ##, se não tiver o \n não quebra a linha.
print(56, 78, sep='-', end='\n')
print(9, 10, sep='-', end='\n')

# Python diferencia as letras maiusculas e minusculas nos códigos. Exemplo: 'print' e 'Print' são comandos diferentes.
# Os comandos 'sep' e 'end' são ARGUMENTOS nomeados, que determinam o separados dos argumentos e o final da linha.