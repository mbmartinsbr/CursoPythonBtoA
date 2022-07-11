"""
Combinations, Permutations e Product - itertools
combinação - ordem nao importa
permutacao - ordem iimporta
ambos não repetem valores unicos
produto - ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product
pessoas = ['luiz', 'Andre', 'Eduardo', 'leticia', 'fabricio', 'rose']

# for grupo in combinations(pessoas, 2):
#     print(grupo)

# for grupo in permutations(pessoas, 2):
#     print(grupo)

# for grupo in product(pessoas, repeat=2):
#     print(grupo)

for grupo in combinations(pessoas, 3):
    print(grupo)
