"""
zip - unindo iteraveis
zip_longest - itertools
"""
# from itertool import zip_longest
import itertools
indicie = itertools.count()
# codigo...

cidades = ['São Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo', 'Outra']

# codigo...

estados = ['SP', 'MG', 'BA']

# cidades_estados = zip(estados, cidades)
# cidades_estados_longest = itertools.zip_longest(
#     indicie,
#     estados,
#     cidades,
#     fillvalue='Estado'
# )
cidades_estados = zip(
    indicie,
    estados,
    cidades
)

# for valor in cidades_estados:
#     print(valor)

# print(dict(cidades_estados))
# print(list(cidades_estados))
# print(list(cidades_estados_longest))

# for valor in cidades_estados_longest:
#     print(valor)

for indicie, estado, cidade in cidades_estados:
    print(indicie, estado, cidade)
