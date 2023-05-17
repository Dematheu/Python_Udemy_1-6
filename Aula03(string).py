"""
DocString
Python = Linguagem de programação
Tipo de tipagem = Dinâmica / Forte
O que é tipagem Dinâmica? R: Já sabe qual o tipo da info. que você está passando para ele.
str -> string -> texto
Strings são textos que estão dentro de aspas (simples ou duplas).
"""

print(1234)

# Aspas simples
print('Lucas de Matheu') 

# Aspas duplas
print("Lucas de Matheu")  

#Escape
print("Lucas \"de Matheu\"") # A barra invertida '\' é o caractere de escape, que determina que o próximo caractere não seja interpretado.

#r
print(r"Lucas \"de Matheu\"") # O comando r mostra caracteres de escape

# Aspas dentro de aspas (melhor que usar o código de escape, para deixar código mais limpo)
print(1, "Lucas 'de Matheu'")
print(2, 'Lucas "de Matheu"')
