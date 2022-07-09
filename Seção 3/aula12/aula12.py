"""
Geradores, iteradores e iteraveis
"""
#
# lista = [0, 1, 2, 3, 4, 5]

# print(hasattr(lista, '__iter__'))  # funcao nativa, __iter__ se tem o atributo iteravel
#
# lista = 123456
#
# print(hasattr(lista, '__iter__'))  # funcao nativa, __iter__ se tem o atributo iteravel
#
# lista = '123456'
#
# print(hasattr(lista, '__iter__'))  # funcao nativa, __iter__ se tem o atributo iteravel

# lista = iter(lista)  # transforma a lista em iterador
#
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
# print(next(lista))
#
# print(hasattr(lista, '__next__'))# funcao nativa, __next__ se tem o atributo iterador

# for v in lista:
#     print(v)

import sys
import time


# lista = list(range(1000))
#
# # sys.getsizeof() Pega a quantidade de memoria que a lista está consumindo
# print(sys.getsizeof(lista))

# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
# def gera():
#     variavel = 'valor1'
#     yield variavel
#     variavel = 'valor2'
#     yield variavel
#     variavel = 'valor3'
#     yield variavel
#
#
# g = gera()
# print(g)

# print(hasattr(g,'__next__'))
# print(hasattr(g,'__iter__'))

# for v in g:
#      print(v)

# print(next(g))
# print(next(g))
# print(next(g))


# lista = list(range(1000))  # 8056
# lista = [x for x in range(1000)]  # 8856
lista = (x for x in range(1000))  # 104
print(sys.getsizeof(lista))
