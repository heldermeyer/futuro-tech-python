"""
Control de Estoque de Produtos
"""

menu = f"""
{"=" * 12} MENU {"=" * 12}
[1] Incluir produtos
[2] Alterar produtos
[3] Excluir Produtos
[4] Listar Produtos

[Q] Sair do Sistema
{"=" * 30}
""" 
 
lista_produtos = []

while True:
    opcao = str(input(f"{menu}=> ")).lower().strip()

    match opcao:
        case "1": # CREATE
            codigo_produto = int(input("Digite o código do produto: "))
            nome_produto = str(input("Digite o nome do produto: ")).upper().strip()
            preco_produto = float(input("Digite o preço do produto: "))
            quantidade_produtos = int(input("Digite a quantidade de produtos: "))

            produto = [codigo_produto, nome_produto, preco_produto, quantidade_produtos]
            lista_produtos.append(produto)
            
            print("Produto cadastrado com sucesso!")
        case "2": # UPDATE
            pass
        case "3": # DELETE
            # codigo_excluir = int(input("Digite código do produto a excluir: "))
            # for indice in range(len(lista_produtos)):
            #   if cod_excluir == lista_produtos[indice][0]:
            #       lista_produtos.pop(indice)
            codigo = int(input("Informe o código do produto: "))
            index_produto = [lista_produtos.index(produto) for produto in lista_produtos if produto[0] == codigo]
            print(f"Produto {lista_produtos[index_produto[0]][1]} excluído com sucesso!")
            lista_produtos.pop(index_produto[0])
        case "4": # READ
            print(f"\n{"=" * 10} PRODUTOS {"=" * 10}")
            for produto in lista_produtos:
                print(f"Código: {produto[0]}\nProduto: {produto[1]}\nPreço: R${produto[2]:.2f}\nQuantidade: {produto[3]}")
                print(f"{"="*30}")
        case "q":
            print("Sistema finalizado.")
            break
        case _: 
            print("Opção inválida!")

    
