# Dicionário (dict): é uma coleção, assim como as listas e as tuplas. Porém, enquanto as tuplas eram indexadas por um índice, os dicionários são indexados
# por chaves. Todo elemento em um dicionário possui uma chave e um valor. Chaves tipicamente são strings, valores podem ser qualquer tipo de dado.

# Criando um Dicionário:
dados_cidades = {'Nome': 'São Paulo',
                 'Estado': 'SP',
                 'area KM': 1521,
                 'populações_milhoes': 12.18
                 }
print(dados_cidades)
print()

# Adicionando valores no Dicionário:
dados_cidades['país'] = 'Brasil'
print(dados_cidades)

# Acessando um valor no dicionário:
print(dados_cidades['Nome'])

# Alterar dados do dicionário:
dados_cidades['area KM'] = 1500
print(dados_cidades)

# Fazendo uma cópia do dicionário:
dados_cidades2 = dados_cidades.copy()
dados_cidades2['Nome'] = 'Santos'
print(dados_cidades)
print(dados_cidades2)

# Atualizando um dicionário:
novos_dados = {
    'populações_milhoes': 15,
    'Fundação': '25/01/1554'
}
dados_cidades.update(novos_dados)
print(dados_cidades)

# Método get() em um valor que não possui no dicionário, retorna None; a busca por colchete, caso não tenha, dá erro:
print(dados_cidades.get('Prefeito'))

# Método key() retorna uma lista de chaves de um dicionário, ou seja, transforma um dicionário em uma lista:
print(dados_cidades.keys())

# Método values() retorna uma lista de valores de um dicionário, ou seja, transforma um dicionário em uma lista:
print(dados_cidades.values())

# Método items() retorna uma lista de tuplas (chave, valor) de um dicionário, ou seja, transforma um dicionário em uma lista:
print(dados_cidades.items())

# O dicionário é definido pelos símbolos { e }

dicionario = {}

# O dicionário não possui um "append".
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'

print(dicionario)
print(type(dicionario))

# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)
print()
# Saída: {'cat': 'gato', 'dog': 'cão', 'mouse': 'rato'}

# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)
print()
# Saída: {'Curso': 'Python Pro', 'Linguagem': 'Python', 'Módulo': 2}

# Podemos utilizar o operador "in" para verificar se uma chave existe:
if 'cat' in dicionario:
    print('cat existe!') # Sim
if 'bird' in dicionario:
    print('bird existe!') # Não
if 'gato' in dicionario:
    print('gato existe!') # Não

#Também podemos utilizar as funções .keys() e .values() para obter listas
#com apenas as chaves ou apenas os valores do dicionário.
chaves = dicionario.keys()
print(chaves)
# Saída: dict_keys(['cat', 'dog', 'mouse'])

valores = dicionario.values()
print(valores)
# Saída: dict_values(['gato', 'cão', 'rato'])

# Já a função .items() retorna uma lista de tuplas (chave, valor) de um dicionário
itens = dicionario.items()
print(itens)
# Saída: dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])
