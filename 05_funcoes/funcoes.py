"""
Funções, Expressões lambda, sorted(), sum(), filter(), map(), reduce(), len()
"""

# UDF (User Defined Function - Funções definidas pelo usuário)

# Calcular a média aritmética de 2 valores:

def soma(a: float, b: float) -> float:
    return a + b

def media(a: float, b: float) -> float:
    return soma(a,b)/2

valor1 = float(input("Digite o primeiro valor: "))
valor2 = float(input("Digite o segundo valor: "))
resultado = media(valor1,valor2)

print(f"Resultado: {resultado}")

# SOLID
# Deve evitar na criação de funções; comando I/O (Input/Output)