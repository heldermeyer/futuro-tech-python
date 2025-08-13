total = 0
valor = 1

while valor != 0:
    valor = float(input("Informe o valor do produto: "))
    total += valor

print(f"Total: R${total:.2f}")