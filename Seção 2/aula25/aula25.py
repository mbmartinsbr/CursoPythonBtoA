"""
* Enumerate - enumerar elementos da lista # list
"""
#         0      1       2
# Tuplas são listas dentro de listas
lista = [
    ['Edu', 'João', 'Luiz'],
    ['Maria', 'Aline', 'Joana'],
    ['Helena', 'Ed', 'Lu']
]

# print(lista[2])
# print(lista[1][2])
enumerada = list(enumerate(lista))

# print(enumerada[1][1])

for v1, v2 in enumerada:
    print(v1, v2)

for v1 in list(enumerate(lista, 53)):
    # print(v1)
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    # print(valor_enumerado, minha_lista)
    print(valor_enumerado, nome1, nome2, nome3)
