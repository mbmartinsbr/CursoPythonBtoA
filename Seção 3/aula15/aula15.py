"""
Count - itertools - infinito
"""
from itertools import count

# contador = count(start=-1, step=-1)
contador = count()
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# print(next(contador))
# for valor in contador:  # infinito
#     print(round(valor, 2))
#     if valor >= 10 or valor <= -10:
#         break

lista = ['Luiz', 'Joao', 'Maria', 'jose', 'silva', 'eduardo']
lista = zip(contador, lista)
print(list(lista))
