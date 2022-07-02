"""
Expressoes lambda (funções anonimas) em Python
"""

# a = lambda x, y: x * y
#
# print(a(2, 2))

lista = [
    ['P1', 13],
    ['P2', 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8]
]

# def func(item):
#     return item[1]
#
#
# lista.sort(key=func, reverse=True)
# lista.sort(key=lambda item: item[1], reverse=True)
print(sorted(lista, key=lambda i: i[0], reverse=True))
print(lista)
