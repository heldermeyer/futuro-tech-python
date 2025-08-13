"""
Listas: variáveis de múltiplas posições
"""

lista_produtos = []
lista_clientes = ["Pedro", "Ana", "Martha"]
lista_vazia = list()

# CRUD (Create, Read, Update, Delete)

# Incluir dados em uma Lista:

lista_produtos.append("Parafuso 3/8")
print(lista_produtos)

lista_clientes.append("Henrique")
print(lista_clientes)

# Alterar (atualizar) lista

lista_clientes[1] = "Ana Maria"
print(lista_clientes)

# Excluir da lista

# del lista_clientes[0]
backup = lista_clientes.pop(0)
print(lista_clientes)
print(f"Backup = {backup}")

# Matriz e Listas

matriz = [["Ana", 22, 1.65],
          ["Pedro", 27, 1.76],
          ["Martha", 34, 1.78]
         ]

print(matriz[1][2])

for pessoa in matriz:
    print(f"\nNome: {pessoa[0]}\nIdade: {pessoa[1]}\nAltura: {pessoa[2]}")

print(f"\n{', '.join(pessoa[0] for pessoa in matriz)}")

lista_numeros = list(range(1, 101, 2))

print(lista_numeros)

# lista_numeros2 = [int(n) for n in range(1, 11)]
# print(lista_numeros2)

