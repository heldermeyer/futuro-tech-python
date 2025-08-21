# Sub programa, rotina, procedimento:

def incluir_produtos():
    descricao = input("Digite a descrição do produto: ").strip().upper()
    preco = float(input("Digite o preço do produto: "))
    return descricao, preco

descricao, preco = incluir_produtos()

print(f"Descrição: {descricao}")
print(f"Preço: {preco}")