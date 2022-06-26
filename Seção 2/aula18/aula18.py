"""
While em python
utilizado para realizar ações enquanto
uma condição for verdadeira.

requisitos: Entender condições e operadores
"""
# x = 0
# while x < 5:
#    if x == 3:
#        x = x + 1
#        continue  # Continue pula para o proximo laço
#        # break termina o Loop ao chegar finaliza a repeticao
#    print(x)
#    x = x + 1

# print('\nFim!')

# x = 0  # coluna
# while x < 10:
#     y = 0  # linha
#     while y < 5:
#         print(f'({x}, {y})')
#         y += 1
#     x += 1

while True:
    print()
    num1 = input('Digite um numero: ')
    num2 = input('Digite outro numero: ')
    operador = input('Digite um operador: ')  # + - / *
    sair = input('Deseja sair? [s]im ou [n]ão: ')
    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um numero')
        continue

    num1 = int(num1)
    num2 = int(num2)

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '/':
        print(num1 / num2)
    elif operador == '*':
        print(num1 * num2)
    else:
        print('Operador invalido')

print('Acabou')


# while True:
#     # ... seu codigo...  # tem que estar em um tab para ficar dentro do while
#     sair = input('Deseja sair Y/N: ')
#     if sair == 'Y':
#         break
