a = 0
b= None
c = False
d = []
e = {}
f = 22
nome = input('Qual seu nome? ')

# if nome:
#     print(nome)
# else:
#     print('Voce nao digitou nada :( ')

variavel = a or b or c or d or e or f or nome

print(nome or None or False or '0' or 'Voce não digitou nada')

print(variavel)
