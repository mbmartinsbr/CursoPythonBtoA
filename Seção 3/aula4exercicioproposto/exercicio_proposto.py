"""
1 - Crie uma função1 que recebe uma função2 como parametro e retorne o valor da função2 executada.
"""


def function1(args):
    print(args)


def function2():
    value = 'Function 2 executed'
    return value


function1(function2())

"""
2 - Crie uma funcao1 que recebe uma funcao2 como parametro e retorne o valor da funcao2 executada.
Faca a funcao1 executar duas funçoes que recebam um numero diferente de argumentos.
"""


def function3(args):
    print(args)
    print(say_hi('Matheus'))
    print(greeting('Matheus', 'Hello'))


def function4():
    value = 'Function 4 executed'
    return value


def say_hi(name):
    return f'Hi {name}'


def greeting(name, greet):
    return f'{greet, name}'


function3(function4())
