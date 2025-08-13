# Entrada dados

lista_produtos = []

for produto in range(5):
    lista_produtos.append(input("Digite o nome do produto: "))

print(f"{", ".join(str(produto) for produto in lista_produtos)}")