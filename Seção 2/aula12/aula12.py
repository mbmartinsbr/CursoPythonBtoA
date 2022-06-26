"""
Operadores logicos
and, or, not
in e not in
"""

nome = 'Luiz Otávio'

# if 'vio' not in nome:
#     print('executei')
# else:
#     print('existe')

usuario = input('Nome de usuario: ')
senha = input('Senha do usuario: ')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuario ou senha invalidos.')
