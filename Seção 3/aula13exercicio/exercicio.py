
carrinho = []

carrinho.append(('produto1', 30))
carrinho.append(('produto1', 20))
carrinho.append(('produto1', 50))

print(sum((produto[1] for produto in carrinho)))

# solucao

total = sum([float(y) for x, y in carrinho])
print(carrinho)
print(total)

