"""
For in em Python
Iterando strings com for
Funcao range (start=0, stop, step= 1)
"""
texto = 'Python'

# c = 0
# while c < len(texto):
#     print(texto[c])
#     c += 1

# for n, letra in enumerate(texto):
#     print(n, letra)

# for numero in range(0, 100, 8):
#     print(numero)
#
# for n in range(100):
#     if n % 8 == 0:
#         print(n)

nova_string = ''
for letra in texto:
    if letra == 't':
        # continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        # break
    else:
        nova_string += letra

print(nova_string)
