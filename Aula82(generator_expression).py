import sys

# Generator expression, Iterables e Iterators em Python
iterable = ['EU', 'Tenho', '__iter__']
iterator = iter(iterable)  # tem __iter__ e __next__

# print(next(iterator))
# print(next(iterator))

# for proximo in iterator:
#     print(proximo)

lista = [n for n in range(1000000)]
generator = (n for n in range(10000))   # generator não tem tamanho, nem indicies.
print(sys.getsizeof(generator))
print(sys.getsizeof(lista))

