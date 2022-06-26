"""
Operadores Relacionais
== Igualdade
> Maior que
>= Maior igual ou igualdade a
< Menor que
<= Menor que ou igual a
!= Diferente
"""
# print(2 == 2)
# print(2 == 1)

num_1 = 2
num_2 = 2

expressao = (num_1 != num_2)

# print(expressao)

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
idade = int(idade)
# Limite para pegar emprestimo
idade_menor = 20  # Muito Jovem
idade_maior = 30  # Passou a idade

if idade >= idade_menor and idade <= idade_maior:
    print(f'{nome} pode pegar o empréstimo. ')
else:
    print(f"{nome} Não pode pegar o empréstimo. ")