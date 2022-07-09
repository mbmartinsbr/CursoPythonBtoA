"""
Dictionary Comprehension
"""

lista = [
    ('chave', 'valor'),
    ('chave2', 'valor2')
]

# d1 = {x.upper(): y.upper() for x, y in lista}
# == d1 = dict(lista)

d1 = {f'chave_{x}': x**2 for x in range(5)}

print(d1, type(d1))
