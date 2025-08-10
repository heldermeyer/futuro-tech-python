# Estrutura de decisão condicional

# Exemplo 2: Criar um programa que imprime a aprovação ou não do estudante

# p1 = float(input("Digite a NOTA da Prova 1: "))
# p2 = float(input("Digite a NOTA da Prova 2: "))
# media (p1+p2)/n

nome = input("Informe o seu nome: ").strip().capitalize()
string_notas = input("Digite as suas notas: ")
notas = [float(nota) for nota in string_notas.split()]
media = sum(notas)/len(notas)

if media >= 6:
    print(f"{nome}, sua média foi {media:.1f}. Você está Aprovado!")
else:
    print(f"{nome}, sua média foi {media:.1f}. Você está Reprovado!")

print(notas)