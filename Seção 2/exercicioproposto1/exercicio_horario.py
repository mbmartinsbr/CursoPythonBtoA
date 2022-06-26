horario = input('informe o horario cheio: ')

try:
    horario = int(horario)

    if horario >= 0 and horario <= 11:
        print('Bom dia')
    elif horario > 11 and horario < 18:
        print('Boa tarde')
    elif horario >= 18 and horario <= 23:
        print('Boa Noite')
    else:
        print('Horario invalido')
except:
    print('Não é um numero inteiro.')