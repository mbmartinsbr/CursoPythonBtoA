nome = 'Luiz'
idade = 32  # int
altura = 1.80  # float
e_maior = idade > 18  #bool True ou False
peso = 80
imc = peso / (altura ** 2)

# print(nome, 'tem', idade, 'de idade e seu imc é de: ', imc)
# print(f'{nome} tem {idade} de idade e seu imc é: {imc:.2f}')  # :.2f Formata ponto flutuante com duas casas
# print('{0} tem {1} anos e seu imc é {2:.2f}'.format(nome, idade, imc))
print('{n} tem {i} anos e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
