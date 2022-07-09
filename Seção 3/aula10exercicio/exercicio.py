string = '01234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
numero_de_letras = 10
lista = [string[indicie:indicie + numero_de_letras] for indicie in range(0, len(string), numero_de_letras)]

print('.'.join(lista))
