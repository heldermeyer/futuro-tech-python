# len() - contar quantidade de caracteres

flag = True

while flag:
    senha = str(input("Digite a nova senha: "))
    if len(senha) < 8:
        print("A senha deve possuir no mínimo 8 caracteres.")
        continue
    elif senha.isnumeric() or senha.isalpha():
        print("A senha deve conter letras e números.")
        continue
    flag = False

print(f"Senha: {senha}")