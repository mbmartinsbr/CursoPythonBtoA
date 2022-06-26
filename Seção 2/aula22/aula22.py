"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
#         0   1    2    3    4   5
# lista = ['a', 'b', 'c', 'd', 'e', 10.5]
# lista[5] = 'Qualquer outra coisa.'
# string = 'ABCDE'

# print(lista[::-1])  # Reverter lista
# print(lista[::-1])
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
# print(l2)
# # l1.extend('a')
# #  l2.append('b')
# l2.insert(0, 'banana')
# print(l2)
# # print(l1)
# l2.pop()
# print(l2)
#     0  1  2  3  4  5  6  7  8
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# print(max(l2))
# print(min(l2))

# l2 = list(range(0, 100, 8))
# l2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# soma = 0
# for valor in l2:
#     soma += valor
#     # print(valor)
# print(soma)
secreto = 'perfume'
digitadas = []
chances = 3

while True:
    if chances <= 0:
        print('Voce perdeu!')
        break

    letra = input('Digite uma letra: ')
    if len(letra) > 1:
        print('Isso não vale digite apenas uma letra.')
        continue

    digitadas.append(letra)
    if letra in secreto:
        print(f'Acertou, a letra {letra} existe na palavra secreta')
    else:
        print(f'A letra {letra} não existe na palavra secreta.')
        digitadas.pop()

    secreto_temporario = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '+'

    if secreto_temporario == secreto:
        print(f'Voce ganhou! A palavra é {secreto_temporario}.')
        break
    else:
        print(f'A Palavra secreta está assim: {secreto_temporario}.')
    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem {chances} chances.')
    print()
