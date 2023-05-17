# Encapsulamento (modificadores de acesso: public, protected, private)
# Python NÃO TEM modificadores de acesso
# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar
# _ (um underline) = protected
#       SÓ DEVE ser acessado dentro da classe e subclasses;
#       NÃO DEVE ser usado fora da classe
#       ou suas subclasses.
# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
'       só DEVE ser usado na classe em que foi'
'       declarado.'

from functools import partial

class Foo:
    def __init__(self):
        self.public = '***Público***'        # Usado em qualquer lugar.
        self._protected = '***Protegido***'  # Usado somente na classe e subclasses.
        self.__private = '***Privado***'     # Usado somente na classe.
        
    def metodo_publico(self):
        # self._metodo_protegido()
        return 'metodo_publico'
        
    def _metodo_protegido(self):
        print('_metodo_protegido')  
        return 'metodo_protegido'
    
    def __metodo_privado(self):
        print('metodo_privado')  
        return '__metodo_privado'

f = Foo()
print(f.public)
print(f.metodo_publico())
print()
print(f._protected)               # não deve ser usado fora da classe por convenção.
print(f._metodo_protegido())      # não gera nenhum erro, mas é algo de comum acordo entre os programadores.
print()
print(f._Foo__private)            # não deve ser usado fora da classe por convenção.
print(f._Foo__metodo_privado())   # gera erro se escrito como os outros. O próprio Python "muda" o nome. (name mangling)