"""
tee - faz copia do iterador
"""

from itertools import groupby, tee

alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Leticia', 'nota': 'B'},
    {'nome': 'Fabricio', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'Joao', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'Andre', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Jose', 'nota': 'B'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Jose', 'nota': 'B'},
]

ordena = lambda item: item['nota']

alunos.sort(key=ordena)
alunos_agrupados = groupby(alunos, ordena)


for agrupamento, valores_agrupados in alunos_agrupados:
    va1, va2 = tee(valores_agrupados)
    print(f'Agrupamento {agrupamento}')
    for aluno in va2:
        print(f'\t{aluno}')

    quantidade = len(list(va1))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()

'''
# Sem tee (com list)
for agrupamento, valores_agrupados in alunos_agrupados:
  valores = list(valores_agrupados)
  print(f'Agrupamento: {agrupamento}')
  for aluno in valores:
    print(f'\t{aluno}')
  quantidade = len(valores)
  print(f'\t{quantidade} alunos tiraram nota {agrupamento}')
'''
