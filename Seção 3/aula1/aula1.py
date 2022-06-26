"""
Funções - def em Python (parte 1)
"""


def saudacao(msg='Olá', nome='usuario'):
    nome = nome.replace('e', '3')
    msg = msg.replace('e', '3')
    # print(msg, nome)
    return f'{msg} {nome}'


# saudacao(nome='Cherly')
# saudacao('Olá', 'Matheus')
# saudacao('Hello', 'Maria')
# saudacao('Olá', 'Otavio')
variavel = saudacao()
print(variavel)

