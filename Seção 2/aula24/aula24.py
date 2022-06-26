"""
Split, Join, Enumerate em Python
* Split - Dividir uma string # str
* Join - Juntar uiim lista # str
* Enumerate - Enumerar elementos da lista # list / iteraveis
"""
# string = "O Brasil é o pais do futebol, o Brasil é penta."
#
# lista1 = string.split(' ')
# lista2 = string.split(',')
# palavra = ''
# contagem = 0
# # print(lista1)
# # print(lista2)
# for valor in lista2:
#     # print(valor)
#     # print(f'a palavra {valor} apareceu {lista1.count(valor)}x na frase.')
#     qtd_vezes = lista2.count(valor)
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x) ')
# for valor in lista2:
#     print(valor.strip().title())
# string = "O Brasil é penta."
# lista = string.split(' ')
# string2 = ','.join(lista)
#
# print(string)
# print(lista)
# print(string2)

# string = "O Brasil é penta."
# lista = string.split(' ')
# for indice, valor in enumerate(lista):
#     print(indice, valor, lista[indice])

# lista = [
#     [0, 'luiz'],
#     [1, 'joao'],
#     [2, 'maria']
# ]
# print(lista)
# for indice, nome in lista:
#     print(indice, nome)
# Desempacotamento
lista = ['luiz', 'joao', 'maria']
n1, n2, n3 = lista
print(n2)