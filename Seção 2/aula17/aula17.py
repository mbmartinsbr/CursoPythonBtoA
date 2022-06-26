"""
Manipulando strings
* string indices
* fatimaneto de strings [incio:fim:passo]
* funcoes built-in len, abs, type, print, etc....
Essas funcoes podem ser usadas diretamente em cada tipo.

Voce pode conferir tudo isso em:
https://docs.python.org/3/library/stdtypes.html (tipo built-in)
https://docs.python.org/3/library/functions.html (funcoes built-in)
"""
# positivos [012345678]
texto = 'Python_s2'

print(texto[0])

# negativos -[987654321]
url = 'www.google.com.br/'
print(url[:-1])

nova_string = texto[2:6]
print(nova_string)

nova_string = texto[:6]
print(nova_string)

nova_string = texto[7:]
print(nova_string)

nova_string = texto[-9]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[:-2]
print(nova_string)

nova_string = texto[0:6:2]
print(nova_string)

nova_string = texto[0::3]
print(nova_string)

print(len(texto))

for letra in texto:
    print(letra)
