"""
Formatando valores com modificadores

:s - texto (string)
:d - inteiros (int)
:f - numeros de ponto flutuante (float)
:.(numero)f quantidade de casas decimas (float) :.2f
:(caractere)(> ou < ^)(Quantidade)(tipo -s, d ou f)

> - esquerda
< - direita
^ - Centro
"""

num_1 = 10
num_2 = 3
nome = 'Luiz Otavio'

divisao = num_1 / num_2
print('{:.2f}'.format(divisao))
print(f'{divisao:.2f}')

print(f'{nome:s}')


num_0 = 1150
num_3 = 1150
print(f'{num_0:0^10}')
print(f'{num_3:0>10.2f}')
nome2 = 'Otavio Miranda'
nome_formatado = '{:@>15}'.format(nome2)
nome_formatado2 = '{n:0<20}'.format(n=nome2)
print(f'{nome2:#^50}')

print(nome_formatado)
print(nome_formatado2)
nome3 = 'Otavio'
sobrenome3 = 'Miranda'
nome_formatado3 = '{0:$^50} {1:#^50}'.format(nome3, sobrenome3)
print(nome_formatado3)
nome = 'Luiz Otavio MiRANda'
nome = nome.ljust(20, '#')
print(nome.lower())  # minusculo
print(nome.upper())  # maiusculo
print(nome.title())  # Primeiras letras maius
