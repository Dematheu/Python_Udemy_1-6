"format"

a = 'AA'
b = 'BB'
c = 1.1
string = 'a={nome1} b={nome2} c={nome3:.2f} {nome1} {nome3} {nome2}'
formato = string.format(nome1=a, nome2=b, nome3=c)

print(formato)