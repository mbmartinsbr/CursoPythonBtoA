"""
Funções (def) em Python - *args **kwargs -
"""


def func(*args, **kwargs):
    # args = list(args)
    # args[0] = 20
    print(args)
    # for i in args:
    #     print(i)
    # print(args[0])
    # print(args[-1])
    # print(len(args))
    # print(kwargs)
    # print(kwargs['nome'])
    # print(kwargs['sobrenome'])
    idade = kwargs.get('idade')
    if idade:
        print(idade)
    else:
        print('idade não existe')


# lista = [1, 2, 3, 4, 5]
# print(*lista, sep='-')
lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)
