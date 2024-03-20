#dicionario = {
 #   "nome":"Andre",
  #  "altura" : 1.65,
  ##  "profissão" :"desenvolvedor, coordenador"
#}
#print(dicionario)*/


# Iniciando a coleta de dados informados pelo usuario
def retornarProduto():
     textoSaida = f"Nome: {produto['nome']}\nDescrição:{produto['descricao']}\nPeso:" \
                       f"{produto['peso']}\nValor:{produto['valor']}\nLançamento:{produto['lancamento'chave
                                                                                          ]}"
     return textoSaida

produto ={ }

produto ["nome"]= input("Por favor, informe o produto:")
produto ["descricao"]= input("Por favor, informe a descrição do produto:")
produto ["lancamento"]= int(input("Por favor, informe o ano de lançamento do produto: "))
produto ["valor"]= float(input("Por favor, informe o valor produto: "))
produto ["peso"]= float(input("Por favor, informe o peso do produto em kg: "))

#print(produto)

for chave, valor in produto.items():
    print(f"{chave} - {valor}")