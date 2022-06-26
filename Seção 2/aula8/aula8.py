"""
* Criar variaveis para nome(str), idade(int),
* Altura(float) e peso(float) de uma pessoa
* Criar variavel com o ano atual (int)
* obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casa decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""
nome = 'Luiz'
idade = 32
anoAtual = 2019
anoNascimento = anoAtual - idade
# idade = anoAtual - anoNascimento
altura = 1.80
peso = 80.5
imc = peso / (altura * altura)

print(f'Olá {nome}, sua idade é de {idade} anos, pesa {peso}kg, mede {altura} e seu imc é de: {imc:.2f}')
print(f'{nome} Nasceu em {anoNascimento}.')
