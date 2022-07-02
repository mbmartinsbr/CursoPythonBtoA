"""
Tuplas
"""
#
# t1 = (1, 2, 3, 'a', 'Luiz Otávio')
#
# print(t1[2:])

t1 = (1, 2, 3, 4, 5)
t1 = list(t1)
t1[1] = 3000
t1 = tuple(t1)

print(t1)
