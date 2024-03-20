=== fazer manipulações em dicionarios:

--- exemplo dicionario com hash function:  # comandos básicos do dicionario...
exemplo_hashing.py

estudantes = {
    1:"Cristiano",
    2:"Carlos", 
    3:"Carol",
    4:"Maria",
    5:"Dionisio",
    6:"Higor",
    7:"Tulio",
    8:"Roberta",
    9:"Matheus",
    10:"João",
}

=== rodar no terminal

chamar:      Aula python3 -i lista_estudantes.py

>>> type(estudantes) # mostrar que é um dicionario

>>> estudantes # apresentar os valores do dicionario

>>> estudantes.keys() # apresentar as chaves provaveis (busca baseada em O(1)

>>> 9 in estudantes # verificar uma chave, ele sempre procura na chave

>>> estudantes[10]   # como acessar a chave e mostrar o valor (busca baseada em O(1)

>>> estudantes.values() # buscar todos os valores (agora nesse caso ja precisa iterar e buscar varias informações)

>>> estudantes.items()   # como trazer um dict agora uma tupla


===========================================================================
===========================================================================
===========================================================================
===========================================================================


abrir o arquivo......
teste.py

pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')


# Podemos imprimir as keys
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
print(pessoas.keys())

# Podemos imprimir os valores
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
print(pessoas.values())

# Podemos imprimir tudo, no caso 3 tuplas
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
print(pessoas.items())

# Podemos imprimir as keys usando laços
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
for k in pessoas.keys():
    print(k)

# Podemos imprimir os values usando laços
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
for k in pessoas.values():
    print(k)

# Podemos imprimir as keys e o os values usando laços
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
for k in pessoas.items():
    print(k)

# Podemos imprimir as keys e o os values usando laços sem aspas
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
for k, v in pessoas.items():
    print(f'{k} = {v}')

=== deletar pessoas

# Podemos deletar algum valor e chave se desejar
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
del pessoas['sexo']
for k, v in pessoas.items():
    print(f'{k} = {v}')

=== adicionar a lista
# Podemos adicionar a lista se desejarmos
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
pessoas['peso'] = 100
for k, v in pessoas.items():
    print(f'{k} = {v}')


=== mudar nome da pessoa

# Podemos alterar valor se desejar
pessoas = {'nome':'Cristiano', 'sexo':'M', 'idade': 22}
pessoas['nome'] = 'Esdras'
for k, v in pessoas.items():
    print(f'{k} = {v}')
    

===========================================================================
===========================================================================

                              