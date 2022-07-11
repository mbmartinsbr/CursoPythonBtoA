lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

# resultado lista soma = [2,3,4,6,8]

lista_soma_py = zip(lista_a, lista_b)
lista_somada = list(x+y for x, y in lista_soma_py)

# print(lista_somada)

# for val in lista_somada:
#     print(val)

# solucao

# lista_soma = []
# for i in range(len(lista_b)):
# for i, _ in enumerate(lista_b):
#     lista_soma.append(lista_a[i] + lista_b[i])

# print(lista_soma)

lista_soma_sol = [x + y for x, y in zip(lista_a, lista_b)]
print(lista_soma_sol)
