"""
Operador ternario em python
"""
# logged_user = False
#
# # if logged_user:
# #     msg = 'Usuario Logado'
# # else:
# #     msg = 'Usuario precisa logar'
#
# msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'
#
# print(msg)
idade = input('Qual sua idade? ')  # 18

if not idade.isnumeric():
    print('Voce precisa digitar somente numeros')
else:
    idade = int(idade)
    eh_de_maior = (idade >= 18)
    msg = 'Pode acessar' if eh_de_maior else 'Não pode acessar.'
    print(msg)
