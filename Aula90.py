# from sys import path

# import Aula90_package.modulo
# from Aula90_package.modulo import soma_do_modulo
# from Aula90_package import modulo

# # print(*path, sep='\n')
# print(soma_do_modulo(1, 2))
# print(Aula90_package.modulo.soma_do_modulo(1, 2))

# # ----------------------------------------------------------
# from Aula90_package.modulo import soma_do_modulo, fala_oi

# print(__name__)
# fala_oi()
# ------------------------------------------------------------

import Aula90_package
print(Aula90_package.soma_do_modulo(2, 3))
print(Aula90_package.nova_variavel)