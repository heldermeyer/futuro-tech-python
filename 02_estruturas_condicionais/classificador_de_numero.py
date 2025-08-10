# Estrutura de decisão condicional

# Exemplo 1: Criar um programa que verifica se um número é positivo, negativo ou zero

numero = float(input("Digite um número: "))

if numero > 0: 
    print(f"Número {numero}: Positivo")
elif numero < 0: 
    print(f"Número {numero}: Negativo")
else: 
    print(f"Número {numero}: Nulo")