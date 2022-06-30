# variavel = 'valor'
# def func():
#     print(variavel)
# def func2(arg=None):
#     # global variavel  # não é uma boa pratica
#     # variavel = 'outro valor'
#     # print(variavel)
#     arg = arg.replace('v', 'c')
#     return arg
# func()
# outra_variavel = func2(arg=variavel)
# print(outra_variavel)

def func():
    outra_variavel = 'Matheus'
    return outra_variavel
    # variavel = 1234
    # print(variavel)


def func2(arg):
    print(arg)


var = func()
func2(var)
