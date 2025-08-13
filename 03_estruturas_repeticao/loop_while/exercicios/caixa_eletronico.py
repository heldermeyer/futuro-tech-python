saldo = 10000
valor_saque = saldo + 1

while valor_saque > saldo:
    valor_saque = float(input("Informe um valor para saque: R$"))
    
saldo -= valor_saque
print(f"Novo saldo: R${saldo:.2f}")