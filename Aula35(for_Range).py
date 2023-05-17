"""
For + Range  (uma não depende da outra)
range -> range(start, stop, step)
"""

numeros = range(10)                #      // Nesse caso, o  10 é o STOP, o START é   0, e o STEP é  1
# numeros = range(5, 10)           #      // Nesse caso, o  10 é o STOP, o START é   5, e o STEP é  1
# numeros = range(6, 10, 2)        #      // Nesse caso, o  10 é o STOP, o START é   6, e o STEP é  2
# numeros = range(-10, 20, 2)      #      // Nesse caso, o  20 é o STOP, o START é -10, e o STEP é  2
# numeros = range(-10, -20, -1)    #      // Nesse caso, o -20 é o STOP, o START é -10, e o STEP é -1




for numero in numeros:
    print(numero)