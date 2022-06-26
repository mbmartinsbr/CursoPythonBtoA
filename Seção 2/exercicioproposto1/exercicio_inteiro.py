num1 = input('Informe um numero inteiro: ')

try:
    num1 = int(num1)

    if (num1 % 2) == 1:
        print(f'{num1} é impar')
    else:
        print(f'{num1} é par')

except:
    print('Não é um numero inteiro.')

'''
if num1.isdigit():
    pass
else:
    print('Isso não é um numero inteiro.')
'''