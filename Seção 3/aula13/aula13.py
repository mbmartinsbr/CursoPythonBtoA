#  Iteradores e geradores depois de utilizado eles "acabam" utilizou a aprimeira vez na segunda so fica o "resto"
nome = 'Luiz Otavio'

# for letra in nome:
#     print(letra)

iterador = iter(nome)

# try:
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
#     print(next(iterador))
# except:
#     pass

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('Olha o for')
for letra in gerador:
    print(letra)