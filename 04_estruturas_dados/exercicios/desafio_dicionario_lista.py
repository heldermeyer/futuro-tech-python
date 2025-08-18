clientes = {
    "nomes": ["Vinicius","Ana","Carla"],
    "idades": [55, 22, 33],
    "alturas": [1.78, 1.66, 1.59],
    "tem_cnh": [True, False, True],
    "dependentes": [
        {
        "conjungue": "Marilda",
        "filhos": ["Henrique", "Márcia"]
        },
    ]
}

for filho in clientes["dependentes"][0]["filhos"]:
    print(filho)

# print(clientes["nomes"][2]) # Carla
# print(clientes["alturas"][1]) # 1.66