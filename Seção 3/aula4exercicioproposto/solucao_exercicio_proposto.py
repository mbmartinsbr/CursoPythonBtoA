"""
1 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada.
"""

# def ola_mundo():
#     return 'Ola mundo!'
#
#
# def mestre(funcao):
#     return funcao()
#
#
# executando = mestre(ola_mundo)
# print(executando)

"""
2 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.
Faca a funcao1 executar duas funçoes que recebam um numero diferente de argumentos.
"""


def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


def fala_oi(nome):
    return f'Oi {nome}'


def saudacao(nome, saudacao):
    return f'{saudacao}, {nome}'


executando = mestre(fala_oi, 'Luiz')
executando2 = mestre(saudacao, 'Luiz', saudacao='Bom dia')
print(executando)
print(executando2)
