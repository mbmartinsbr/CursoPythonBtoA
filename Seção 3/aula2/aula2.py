"""
Funcoes (def) em Python - return (parte 2)
"""


def divisao(n1, n2):
    if n2 == 0:
        return
    return n1 / n2


divide = divisao(8, 2)
if divide:
    print(divide)
else:
    print('conta invalida')


def f(var):
    print(var)


def dumb():
    return f
    # return [1, 2, 3, 4, 5]


var = dumb()('teste')
print(type(f))
print(id(var), id(f))


def dumb2():
    return ('Matheus', 'Martins')


var = dumb2()

print(var[0], var[1], type(var))
