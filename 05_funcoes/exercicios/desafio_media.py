# Refatorar a função média para "n" números

def media(string_numeros):
    numeros = [float(numero) for numero in string_numeros.split()]
    return sum(numeros)/len(numeros)

string_numeros = str(input("Digite os números: "))

print(f"Média: {media(string_numeros):.2f}")

exit()

def media(numeros: list) -> float:
    """Essa função recebe o parâmetro "numeros",\n 
    que geralmente é uma lista contendo números\n
    e retorna a média desses números."""
    return sum(numeros)/len(numeros)

numeros = []

n = int(input("Digite quantos números você quer somar: "))
for i in range(n):
    numeros.append(float(input(f"{i+1}. Digite o número: ")))
print(f"Média: {media(numeros):.2f}")
