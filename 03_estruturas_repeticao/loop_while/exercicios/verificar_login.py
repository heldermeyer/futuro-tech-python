
LOGIN = "helder"
PASSWORD = "123456"

while True:
    usuario = str(input("Usuário: "))
    senha = str(input("Senha: "))
    if usuario != LOGIN:
        print("Usuário ou senha incorretos!")
        continue
    elif senha != PASSWORD:
        print("Senha incorreta!")
        continue
    print("Login realizado com sucesso!")
    break