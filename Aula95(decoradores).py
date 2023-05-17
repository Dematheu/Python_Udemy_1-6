# Funções decoradoras e decoradores
# Decorar = adicionar / Remover / restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.
# Decoradores são "Syntax Sugar" (Açucar Sintático)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('vou decorar')
        for arg in args:
            is_string(arg)
        resultado = func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}.')
        print('decorada')
        return resultado
    return interna

@criar_funcao
def inverte_string(string, *args, **kwargs):
    print(f'{inverte_string.__name__}')
    return string[::-1]

def is_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


invertida = inverte_string('123')
print(invertida)
