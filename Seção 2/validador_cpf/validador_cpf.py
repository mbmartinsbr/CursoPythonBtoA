"""
CPF = 168.995.350-09
16899535009
1 * 10 = 10         |    1 * 11 = 11<-
6 * 9 = 54          |    6 * 10 = 60
8 * 8 = 64          |    8 * 9 = 72
9 * 7 = 63          |    9 * 8 = 72
9 * 6 = 54          |    9 * 7 = 63
5 * 5 = 25          |    5 * 6 = 30
3 * 4 = 12          |    3 * 5 = 15
5 * 3 = 15          |    5 * 4 = 20
0 * 2 = 0           |    0 * 3 = 0
                    | -> 0 * 2 = 0
        297         |            343
11-(297 % 11) = 11  | 11-(343%11 = 9
11>9 = 0            |
Digito 1 = 0        | Digito 2 = 9
"""
while True:
    cpf_str = input('Informe seu CPF ')
    sum_dig1 = 0
    sum_dig2 = 0
    cpf = cpf_str.replace('.', '').replace('-', '')
    for p, r in enumerate(range(10, 1, -1)):
        sum_dig1 += int(cpf[p]) * r
        sum_dig2 += int(cpf[p]) * (r + 1)
    dig1_calc = 11 - (sum_dig1 % 11)
    digit1 = dig1_calc if not dig1_calc > 9 else 0
    dig2_calc = 11 - (sum_dig2 % 11)
    digit2 = dig2_calc if not dig2_calc > 9 else 0
    if int(cpf[-2]) == int(digit1) and int(cpf[-1]) == int(digit2):
        print(f'CPF {cpf_str} é valido')
    else:
        print(f'CPF {cpf_str} é Invalido')