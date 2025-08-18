# Criar um dicionário de dados para armazenar informações de produtos
# (Ex: preço, quantidade, validade, peso...)

from datetime import date

# produto = {
#     "codigo": 1,
#     "descricao": "Batata",
#     "preco": 0.59,
#     "validade": date(2025, 9, 10),
#     "quantidade": 123,
#     "unidade": "Kg",
#     "em_estoque": True,
#     "peso": 1
# }

# print(f"O produto {produto["descricao"]} tem o peso de {produto["peso"]} \
#     {produto["unidade"]}")

# print("Meu produto:\n")
# for chave, valor in produto.items():
#     print(f"{chave.title()}: {valor}")

def convert_string_to_boolean() -> bool:
    while True:
        value = str(input("Informe se o produto está em estoque (Sim ou Não): "))
        if value.upper().strip() in ["SIM","S"]:
            return True
        elif value.upper().strip() in ["NÃO","N"]:
            return False
        else:
            print("Digite Sim ou Não.")
            continue

dia = int(input("Informe o DIA (1 a 31): ").strip())
mes = int(input("Informe o MÊS (1 a 12): ").strip())
ano = int(input("Informe o ANO (AAAA): ").strip())
# mes = mes if len(mes) == 2 else "0" + mes

produto:dict = {
    "codigo": int(input("Informe o código do produto: ")),
    "descricao": str(input("Informe a descrição do produto: ")).title().strip(),
    "preco": 8.76,
    "validade": date(ano, mes, dia),
    "quantidade": 200,
    "unidade": "Kg",
    "em_estoque": convert_string_to_boolean(),
    "peso": 1
}

print(f'Produto: {produto["descricao"]} - Código: {produto["codigo"]}')
print(f'Peso: {produto["peso"]} {produto["unidade"]}')
print(f'Preço: R${produto["preco"]:.2f} a unidade e R${produto["preco"] * produto["quantidade"]:.2f} total.')

def generator():
    with open("log.txt", "r", encoding="utf-8", newline="") as file:
        for line in file:
            yield line

for linha in generator():
    print(linha.strip())