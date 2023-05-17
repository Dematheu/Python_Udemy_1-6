import importlib

import aula89_mod

# Singleton : Quando só pode existir uma instância de determinada coisa no Python.
# Import: quando você importa, o Python já salva isso na memória, e não executa novamente.

print(aula89_mod.variavel)

for i in range(10):
    importlib.reload(aula89_mod)  # Recarrega o modulo se quiser
    print(i)

print('Fim')