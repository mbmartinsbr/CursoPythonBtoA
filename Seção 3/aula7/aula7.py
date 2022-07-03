"""
Dicionarios
"""
# d1 = {'chave1':'valor da chave'}
# d1 = dict(chave1='valor da chave', chave2='valor da outra chave')
# d1 = {1: 'valor', 2: 'valor', 3: 'valor real'}
# d1['nova chave'] = 'Valor da nova chave'

# d1 = {
#     'chave1': 'valor',
#     'chave2': 'outro valor',
#     'chave3': 'tupla',
#
# }
# d1['naoexiste'] = 'agora existe'
# if 'naoexiste' in d1:
# print(d1['naoexiste'])
# d1['str']='agora existe'
# d1.update({'nova_chave':'novo valor'})
# if d1.get('nova_chave') is not None:
#     print(d1.get('nova_chave'))
#
# print('oii')
# del d1['str']

# print('str' in d1)
# print('str' in d1.keys())
# print('valor' in d1.values())

# print(len(d1))

# for k,v in d1.items():
#     # print(k[0], k[1])
#     print(k, v)

# clientes ={
#     'Cliente1' : {
#         'Nome':'Luiz',
#         'sobrenome': 'Otavio'
#     },
#     'Cliente2': {
#         'Nome': 'João',
#         'sobrenome': 'Moreira'
#     },
#     'Cliente3': {
#         'Nome': 'Maria',
#         'sobrenome': 'Moreira'
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'\t {dados_k} = {dados_v}')
# import copy
#
# d1 = {1: 'a', 2: 'b', 3: 'c', 'd': ('luiz', 'otavio')}
# # v = d1
# v = d1.copy()
# # v = copy.deepcopy(d1)
# v[1] = 'Luiz'
#
# # v['d'][0] = 'Joaozinho'
# v['d'] = ('Otavio', 'Luiz')
#
# print(d1)
# print(v)
# print(d1 == v)

# lista = (  # [
#     ['c1', 1],
#     ['c2', 2],
#     ['c3', 3],
#     # ('c2', 2),
#     # ('c1', 1),
#     # ('c3', 3),
# )
# # ]
# d1 = dict(lista)
# print(d1['c3'])
d1 = {
    1: 2,
    2: 3,
    4: 5,
}
d2 = {
    'a': 'b',
    'c': 'd',
}
# d1.pop(4)
# d1.popitem()

print(d1)
print(d2)
d1.update(d2)

print(d1)
