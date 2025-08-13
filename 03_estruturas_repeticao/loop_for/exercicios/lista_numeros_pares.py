# Gere uma variável do tipo "lista" que contenha os números pares de 0 à 200:
numeros_pares = [int(n) for n in range(0,201,2)]
print(numeros_pares)

numeros_pares2 = list(range(101))
print(f"\n{numeros_pares2[::2]}")

for numero in numeros_pares:
    quadrado = numero ** 2
    print(f"Número: {numero} - Quadrado: {quadrado}")

k = []
for j in range(11):
    print(j, end=" ")
    k.append(j)
    
print(f"\n{', '.join(str(num) for num in k)}")