# Sistema de Promoções para E-commerce

# Uma loja online quer aplicar descontos diferentes com base no tipo de produto.

# Crie uma função que receba uma lista de diversos dicionários contendo o nome do produto, o preço,
# e a categoria, e aplique um desconto de:

# 10% para produtos eletrônicos
# 5% para roupas
# 0% para outros

# A função deve retornar uma nova lista com os produtos atualizados, incluindo um campo
# adicional "preco_com_desconto"

def calcular_desconto(produto: float, percentual: float) -> float:
    return (produto - (produto * percentual))

def aplicar_desconto(lista_produtos: list) -> list:
    produtos_desconto = lista_produtos.copy()
    for i, produto in enumerate(lista_produtos):
        if produto["categoria"] == "Eletrônicos":
            produtos_desconto[i]["preco_com_desconto"] = calcular_desconto(produto["preco"], 0.10)
        elif produto["categoria"] == "Roupas":
            produtos_desconto[i]["preco_com_desconto"] = calcular_desconto(produto["preco"], 0.05)
        else:
            produtos_desconto[i]["preco_com_desconto"] = calcular_desconto(produto["preco"], 0)

    return (produtos_desconto)

lista_produtos = [
    {
        "produto": "Carregador",
        "preco": 19.90,
        "categoria": "Eletrônicos"
    },
    {
        "produto": "Camisa",
        "preco": 39.90,
        "categoria": "Roupas"
    },
    {
        "produto": "Martelo",
        "preco": 7.50,
        "categoria": "Ferramentas"
    }
]

for item in aplicar_desconto(lista_produtos):
    print(f"Produto: {item["produto"]}")
    print(f"Preço: R${item["preco"]:.2f}")
    print(f"Categoria: {item["categoria"]}")
    print(f"Preço (Desconto): R${item["preco_com_desconto"]:.2f}\n" if item["preco_com_desconto"] != item["preco"] else "")
