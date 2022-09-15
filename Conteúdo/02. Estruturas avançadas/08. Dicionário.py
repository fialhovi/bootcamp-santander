#!/usr/bin/env python
# coding: utf-8

# In[1]:


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


# In[3]:


# Adicionando valores no Dicionário:
dados_cidades['país'] = 'Brasil'
print(dados_cidades)


# In[4]:


# Acessando um valor no dicionário:
print(dados_cidades['Nome'])


# In[5]:


# Alterar dados do dicionário:
dados_cidades['area KM'] = 1500
print(dados_cidades)


# In[6]:


# Fazendo uma cópia do dicionário:
dados_cidades2 = dados_cidades.copy()
dados_cidades2['Nome'] = 'Santos'
print(dados_cidades)
print(dados_cidades2)


# In[7]:


# Atualizando um dicionário:
novos_dados = {
    'populações_milhoes': 15,
    'Fundação': '25/01/1554'
}
dados_cidades.update(novos_dados)
print(dados_cidades)


# In[8]:


# Método get() em um valor que não possui no dicionário, retorna None; a busca por colchete, caso não tenha, dá erro:
print(dados_cidades.get('Prefeito'))


# In[9]:


# Método key() retorna uma lista de chaves de um dicionário, ou seja, transforma um dicionário em uma lista:
print(dados_cidades.keys())


# In[10]:


# Método values() retorna uma lista de valores de um dicionário, ou seja, transforma um dicionário em uma lista:
print(dados_cidades.values())


# In[11]:


# Método items() retorna uma lista de tuplas (chave, valor) de um dicionário, ou seja, transforma um dicionário em uma lista:
print(dados_cidades.items())


# In[12]:


# O dicionário é definido pelos símbolos { e }

dicionario = {}


# In[13]:


# O dicionário não possui um "append".
# Adicionamos valores diretamente:

dicionario['cat'] = 'gato'
dicionario['dog'] = 'cachorro'
dicionario['mouse'] = 'rato'


# In[14]:


print(dicionario)
print(type(dicionario))
print()


# In[15]:


# Dicionários, assim como as listas, são mutáveis:
dicionario['dog'] = 'cão'
print(dicionario)
print()
# Saída: {'cat': 'gato', 'dog': 'cão', 'mouse': 'rato'}


# In[16]:


# Podemos criar o dicionário diretamente também:
dicionario2 = {'Curso': 'Python Pro', 'Linguagem':'Python', 'Módulo':2}
print(dicionario2)
print()
# Saída: {'Curso': 'Python Pro', 'Linguagem': 'Python', 'Módulo': 2}


# In[17]:


# Podemos utilizar o operador "in" para verificar se uma chave existe:
if 'cat' in dicionario:
    print('cat existe!') # Sim
if 'bird' in dicionario:
    print('bird existe!') # Não
if 'gato' in dicionario:
    print('gato existe!') # Não


# In[19]:


#Também podemos utilizar as funções .keys() e .values() para obter listas
#com apenas as chaves ou apenas os valores do dicionário.
chaves = dicionario.keys()
print(chaves)
# Saída: dict_keys(['cat', 'dog', 'mouse'])


# In[20]:


valores = dicionario.values()
print(valores)
# Saída: dict_values(['gato', 'cão', 'rato'])


# In[21]:


# Já a função .items() retorna uma lista de tuplas (chave, valor) de um dicionário
itens = dicionario.items()
print(itens)
# Saída: dict_items([('cat', 'gato'), ('dog', 'cão'), ('mouse', 'rato')])


# In[ ]:




