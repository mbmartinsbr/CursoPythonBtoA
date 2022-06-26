"""
For/Else em python
"""

variavel = ['Luiz Otavio', 'jaoozinho', 'Maria']
comeca_com_j = False

for valor in variavel:
    if valor.lower().startswith('j'):
        break
        # comeca_com_j = True

# if comeca_com_j:
#     print('Existe palavra com J')
else:
    print('Não existe palavra com J')
