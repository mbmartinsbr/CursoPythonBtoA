"""
Desempacotamento de listas em Python
"""
lista = ['Luiz', 'Joao', 'Maria',1,2,3,4,5,6,7,8,9,100]
# n1, n2, *outra_lista, ultimo_da_lista = lista  # Gera outra lista com o "Resto" da lista
*outra_lista, n1, n2, n3 = lista  # Fim da lista
# *_ voce não vai utilizar no resto do codigo caso nao queira usar (convensão)
# n1, n2, n3 = lista

print(outra_lista)
