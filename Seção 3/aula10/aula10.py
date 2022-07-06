"""
List Comprehensions
"""


def divisaofn(x, y):
    return x / y


def multiplicacaofn(x, y):
    return x * y


def potenciacaofn(x, y):
    return x ** y


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]

ex2 = [v * 2 for v in l1]

ex3 = [(v, v2) for v in l1 for v2 in range(3)]

l2 = ['luiz', 'mauro', 'maria']
ex4 = [v.replace('a', '@').upper() for v in l2]

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2'),
    ('chave3', 'valor3'),
)
ex5 = [(y, x) for x, y in tupla]
ex5 = dict(ex5)

l3 = list(range(100))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
# print(ex7)

# https://www.youtube.com/watch?v=1YbTDczvqco

numeros = [1, 2, 3, 4, 5]
divisao = [divisaofn(numero, 2) for numero in numeros]
multiplicacao = [multiplicacaofn(numero, 2) for numero in numeros]
quadrado = [potenciacaofn(numero, 2) for numero in numeros]

# print(numeros)
# print(divisao)
# print(multiplicacao)
# print(quadrado)
numeros2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
novos_numeros = [numero for numero in numeros2 if numero>5]
impares = [numero for numero in numeros2 if numero % 2 != 0]
pares = [numero for numero in numeros2 if numero % 2 == 0]
outro_if = [
    numero
    if numero != 6 else 600
    for numero in numeros2
    if numero % 2 == 0
]

# print(numeros2)
# print(novos_numeros)
# print(impares)
# print(pares)
# print(outro_if)

linhas_e_colunas = [
    (x, y)
    if y != 2 else (x, y*1000)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]
# print(linhas_e_colunas)

string = 'Otavio Miranda'
numero_de_letras = 1
nova_string = '.'.join([
    string[indicie:indicie + numero_de_letras] for indicie in range(0, len(string), numero_de_letras)
])

# print(nova_string)

nomes = ['luiz', 'maria', 'helena', 'joana', 'felipe']
# novos_nomes = [nome for nome in nomes]  # title primeira letra maiuscula | lower e upper
novos_nomes = [
    f'{nome[:-1].lower()}{nome[-1].upper()}'
    for nome in nomes
]
# print(novos_nomes)

numeros = [[numero, numero **2] for numero in range(10)]
flat = [y for x in numeros for y in x]
print(numeros)
print(flat)