produtos = []
precos = []

for i in range(5):
    produto = input(f"Digite o {i + 1}º produto: ")
    preco = float(input(f"Digite o preço do {produto}: "))

    produtos.append(produto)
    precos.append(preco)

print("\n=== PRODUTOS CADASTRADOS ===")

for i in range(5):
    print(f"{produtos[i]} - R$ {precos[i]:.2f}")

print("\n=== RESULTADO ===")
print(f"Valor total: R$ {sum(precos):.2f}")
print(f"Maior preço: R$ {max(precos):.2f}")
print(f"Menor preço: R$ {min(precos):.2f}")
