from datetime import datetime
print("Idade: ", 2025-2002) # string
print(f"Idade: {2025-2002} anos") # f-string

# Usando variáveis
# operador de atribuição =
ano_nascimento = int(input("Digite o seu ano de nascimento: "))
idade = int(datetime.today().year) - ano_nascimento
print(f"Você tem {idade} anos.")