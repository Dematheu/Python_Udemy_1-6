# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# Verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy
# 0 0.0 '' False
# Também existe o None que é
# usado para representar um não valor


# Avaliação de curto circuito:
print(True and True and True and True and False and True)
print(bool(0))
print(bool(' '))
print(True and 0 and True)