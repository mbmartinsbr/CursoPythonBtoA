"""
Tipos de dados
str - string - textos 'Assim' "Assim"
int - inteiro - 12331231 0 -10 -20 -50 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - true/false
"""
print('Luiz', type('Luiz'))  # type = retorna tipo do valor
print(10, type(10))  # int
print(25.23, type(25.23))  # float
print(10 == 10, type(10 == 10))  # bool
print(bool(0))

'''
Conversão
no caso da função bool()
0 - '' - False

Qualquer outra coisa é true


int() - converte para inteiro
float() - converte para float
'''
print('luiz', type('luiz'), bool('luiz'))
print('10', type('10'), type(int('10')))
print('10.5', float('10.5'))
print(10+10, '10' + '10')

# String Nome
print('Matheus Braga Martins', type('Matheus Braga Martins'))

# Idade: int
print(32, type(32))

# Altura: Float
print(1.81, type(1.81))

# é Maior de idade 10>20
print(32>18, type(32>18))

