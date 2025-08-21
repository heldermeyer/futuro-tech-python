# Crie uma função para concatenar os dados (argumentos);

def juntar(endereco, bairro):
    return f"{endereco}, {bairro}"

endereco = str(input("Insira o endereço: "))
bairro = str(input("Insira o bairro: "))
resultado = juntar(endereco, bairro)

print(resultado)


