# Cálculo de desconto progressivo
# até 100 reais de desconto
# entre 100,01 e 500 - 5%
# acima de 040: 10%


valor_final = 0
valor_compra = float(input("Informe o valor da compra: "))

def calcular_valor_final(valor_compra: float, porcentagem: float) -> float:
    return valor_compra - (valor_compra * porcentagem)

if valor_compra > 100 and valor_compra <= 500:
    valor_final = calcular_valor_final(valor_compra, 0.05)
elif valor_compra > 500:
    valor_final = calcular_valor_final(valor_compra, 0.10)
else:
    valor_final = valor_compra

print(f"Valor final: R${valor_final:.2f}")
