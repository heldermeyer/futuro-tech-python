"""4. Validação de Login com Duas Condições
Você está criando um sistema simples de login. O usuário deve fornecer:
Um nome de usuário e uma senha.
Considere que o nome de usuário correto é "admin" e a senha correta é "12345".
Mas, por questão de segurança, usuários com nome diferente de "admin" não devem conseguir nem tentar logar, mesmo que a senha esteja correta.
Implemente essa verificação e mostre mensagens como:
"Login realizado com sucesso"
"Senha incorreta"
"Usuário não autorizado"
Use and e not para compor a lógica.
"""

usuario = str(input("Informe o nome do usuário: "))
senha = str(input("Informa a senha: "))

USUARIO_CORRETO = "admin"
SENHA_CORRETA = "12345"
login_sucesso = usuario == USUARIO_CORRETO and senha == SENHA_CORRETA
usuario_nao_autorizado = not (usuario == USUARIO_CORRETO)

if login_sucesso:
    print("[Sistema] Login realizado com sucesso!")
elif usuario_nao_autorizado:
    print("[Sistema] Usuário não autorizado!")
else:
    print("[Sistema] Senha incorreta!")
    