"""
1 - Crie uma função que exibe uma saudacao com os parametro saudacao e nome.
"""


def greet(greeting, name):
    print(f'{greeting} {name}')


# greet('Olá', 'Matheus')

"""
2 - Crie uma funcao que recebe 3 numeros como parametro e exiba a soma entre eles.
"""


def sum(n1, n2, n3):
    print(n1 + n2 + n3)


# sum(1, 2, 3)
# sum(1, 1, 1)
# sum(2, 1, 1)

"""
3 - Crie uma funcao que receba 2 numero. o primeiro é um valor e o segundo é percentual (ex.10).
Retorne (return) o valor do primeiro numero somado do aumento do percentual do mesmo.
"""


def increase(value, percent):
    return value + (value * (percent / 100))


# print(increase(100, 10))
# print(increase(50, 10))
# print(increase(10, 10))
# print(increase(15, 100))

"""
4 - Fizz Buzz - Se o parametro da funcao for divisivel por 3, retorne fizz, 
se o parametro da funcao for divisivel por 5 retorne buzz.
se o parametro for 5 e 3, retorne Fizzbuzz, caso contrario retorne o numero enviado.
"""


def fizzbuzz(value):
    # if value % 3 == 0:
    #     if value % 5 == 0:
    #         return 'FizzBuzz'
    #     else:
    #         return 'Fizz'
    # elif value % 5 == 0:
    #     return 'Buzz'
    # else:
    #     return value
    # Corrected Begin
    if value % 3 == 0 and value % 5 == 0:
        return f'FizzBuzz, {value} é divisivel por 3 e 5.'
    if value % 3 == 0:
        return f'Fizz , {value} é divisivel por 3.'
    if value % 5 == 0:
        return f'Buzz, {value} é divisivel por 5.'
    return value
    # Corrected end


# print(fizzbuzz(10))
# print(fizzbuzz(6))
# print(fizzbuzz(15))
# print(fizzbuzz(22))
# print(fizzbuzz(7))
from random import randint

for i in range(100):
    rand = randint(0, 100)
    print(fizzbuzz(rand))
