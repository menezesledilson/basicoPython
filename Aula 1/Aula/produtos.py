# Função para cadastrar um produto
def cadastrar_produto(codigo, nome, descricao, preco, produtos):
    produtos[codigo] = {
        "nome": nome,
        "descricao": descricao,
        "preco": preco
    }
    print("Produto cadastrado com sucesso!")

# Função para exibir todos os produtos cadastrados
def exibir_produtos(produtos):
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        print("Lista de Produtos:")
        for codigo, produto in produtos.items():
            print("Código:", codigo)
            print("Nome:", produto["nome"])
            print("Descrição:", produto["descricao"])
            print("Preço:", produto["preco"])
            print("--------------------------")

# Dicionário para armazenar os produtos
produtos = {}

# Menu de opções
def menu():
    print("\n===== Cadastro de Produtos =====")
    print("1 - Cadastrar Produto")
    print("2 - Exibir Produtos")
    print("3 - Sair")

# Loop do programa
while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        codigo = input("Digite o código do produto: ")
        nome = input("Digite o nome do produto: ")
        descricao = input("Digite a descrição do produto: ")
        preco = float(input("Digite o preço do produto: "))
        cadastrar_produto(codigo, nome, descricao, preco, produtos)
    elif opcao == "2":
        exibir_produtos(produtos)
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
