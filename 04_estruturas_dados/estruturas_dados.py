"""
Listas (List), Tuplas (Tuple), Dicionários (Dict) e Conjuntos (Set)
"""

# Dicionários (Dict)

def comprar():
    print("Compras efetuadas")
    return True

cliente = {
    "nome": "Helder",
    "idade": 22,
    "altura": 1.78,
    "tem_cnh": True,
    "efetuar_compra": comprar()
}

print(cliente)
print(cliente.keys())
print(cliente.values())
print(cliente.items())

print(f"O cliente {cliente["nome"]} tem CNH: {"Sim" if cliente["tem_cnh"] == True else "Não"}")

if cliente["tem_cnh"]:
    print("Cliente tem CNH")
else:
    print("Cliente não tem CNH")

cliente["efetuar_compra"]

# Inclusão
cliente["saldo"] = 1234.56
print(cliente)
cliente["saldo"] = 9999.88
print(cliente)

# Exclusão dic:
del cliente["idade"]
print(cliente)

# for key, value in cliente.items():
#     print(f"\n{key.title()}: {value}")

exit()

# Conjuntos (Set)

conjunto_nomes = {"Ana","Martha","Carla","Antônio","Ana"}
print(conjunto_nomes)

lista_numeros = [1,2,3,4,5,6,7,8,9,1]
conjunto_numeros = set(lista_numeros)
nova_lista = list(conjunto_numeros)
print(lista_numeros)
print(conjunto_numeros)
print(nova_lista)

# Tuplas (Tuple)

tupla_nomes = ("Ana","Martha","Carla") # Somente leitura (imutável)
print(tupla_nomes[1])
# Usos: enviar dados entre App (API), retorno de funções, argumentos de Classes...abs

exit()

# Listas (List)
lista_nomes = ["Ana", "Pedro", "Maria"]
print(lista_nomes)

# Inclusão:
lista_nomes.append("João")