# Try, except, else, finally
# https://docs.python.org/pt-br/3/library/exceptions.html#built-in-exceptions


try:
    print('ABRIR ARQUIVO')
    # 8 / 0
except ZeroDivisionError:
    print('dividiu 0')
else:
    print('Não deu erro')
finally: # FINALLY VAI SER EXECUTADO SEMPRE, MESMO SE HOUVER ERROS NO TRY
    print('FECHAR ARQUIVO')
