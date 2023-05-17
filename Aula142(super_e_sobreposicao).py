#super() é a super classe na sub classe
# Classe principal (Pessoa)
#   -> super class, base class, parent class
# Classes filhas (Cliente)
#   -> sub class, derived class, child class
# object

# class MinhaString(str):
#     def upper(self):
#         print('Chamou Upper')
#         retorno = super(MinhaString, self).upper()
#         print('Depois do upper')
#         return retorno

# string = MinhaString('Lucas')
# print(string.upper())

class A:
    atributo_a = 'valor a'

    def __init__(self, atributo):
        self.atributo = atributo
        

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'

    def __init__(self, atributo, outra_coisa):
        super().__init__(atributo)
        self.outra_coisa = outra_coisa
        print('init no B')

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('init no C')

    def metodo(self):
        # super().metodo()          # B
        # super(B, self).metodo()   # A
        # super(A, self).metodo()   # object
        print('C')

# print(C.mro())
# print(B.mro())
# print(A.mro())

c = C('oi', 'qualquer')
# print(c.atributo_a)
# print(c.atributo_b)
# print(c.atributo_c)
# c.metodo()
print(c.atributo)
print(c.outra_coisa)