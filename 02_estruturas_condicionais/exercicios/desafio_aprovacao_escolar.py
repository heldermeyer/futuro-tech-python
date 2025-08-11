"""
2. Sistema de Aprovação Escolar

Crie um programa que receba as notas de duas provas de um aluno. O aluno será aprovado se:

A média for maior ou igual a 7 e nenhuma das notas for menor que 4.

Use operadores lógicos para verificar essas condições e exibir se o aluno foi "Aprovado" ou "Reprovado".
"""

while True:

    string_notas = input("Insira as duas notas (Ex: 8.5 7.5): ")
    notas = [float(nota) for nota in string_notas.split()]

    if len(notas) < 2:
        print("Por favor, informe 2 notas (Ex: 8.5 7.5)!")
        continue
    break

menor_4 = any(nota <= 4 for nota in notas)
media = sum(notas)/len(notas)
condicao = media >= 7 and not menor_4

if condicao:
    resultado = "Aprovado!"
elif menor_4:
    resultado = f"Reprovado!\nMotivo: Uma das notas é igual ou menor do que 4."
else:
    resultado = f"Reprovado!\nMotivo: Abaixo da média."

print(f"\nMédia final: {media}\nResultado: {resultado}")