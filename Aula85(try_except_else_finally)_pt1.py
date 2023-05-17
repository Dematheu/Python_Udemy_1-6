# Try, except, else, finally

try:
    a = 18
    b = 0
    print('linha1')
    c = a / b
    print('linha2')
except ZeroDivisionError as e:
    print(e)
    print(e.__class__.__name__)
except NameError:
    print('Nome b não está definido')
except (TypeError, IndexError) as error:
    print('TypeError ou IndexError')
    print('MSG:', error)
    print('Nome:', error.__class__.__name__)
except Exception:
    print('ERRO DESCONHECIDO.')
print('cont')