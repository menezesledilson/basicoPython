def exibirProduto():
    print(f"Nome: {nomeProduto}")
    print(f"Descricao: {descricaoProduto}")
    print(f"Peso: {pesoProduto}")
    print(f"Valor:{valorProduto}")
    print(f"Lançamento: {anoLancamentoProduto}")

    def retornaProduto():
        textoSaida = f"Nome: {nomeProduto}\nDescrição:{descricaoProduto}\nPeso:" \
                       f"{pesoProduto}\nValor:{valorProduto}\nLançamento:{anoLancamentoProduto}"
        return textoSaida


print("Cadastro de produtos")

# Iniciando a coleta de dados informados pelo usuario

nomeProduto = input("Por favor, informe o produto:")
descricaoProduto = input("Por favor, informe a descrição do produto:")
anoLancamentoProduto = int(input("Por favor, informe o ano de lançamento do produto: "))

valorProduto = float(input("Por favor, informe o valor produto: "))
pesoProduto = float(input("Por favor, informe o peso do produto em kg: "))

# Exibir simples das variaveis

# print(nomeProduto)
# print(descricaoProduto)
# print(anoLancamentoProduto)
# print(valorProduto)#
# print(pesoProduto)

# Exibição das variaveis usando texto
# print(f"Nome: {nomeProduto}" )
# print(f"Descricao: {descricaoProduto}")
# print(f"Peso: {pesoProduto}")
# print(f"Valor:{valorProduto}")
# print(f"Lançamento: {anoLancamentoProduto}")
#exibirProduto()
print(retornaProduto())
