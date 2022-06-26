num1 = input('Digite um numero: ')
num2 = input('Digite outro numero: ')

# isnumeric isdigit isdecimal
# numeros e positivos (22312365498)

# print(num2.isnumeric())
# print(num1.isnumeric())
# num1 = int(num1)
# num2 = int(num2)
#
# print(num1 + num2)
# if num1.isdigit() and num2.isdigit():
try:
    num1 = float(num1)
    num2 = float(num2)
    print(num1+num2)
# else:
except:
    print('Não pude converter os numeros para realizar contas.')
