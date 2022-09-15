#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Percorrendo coleções
# O for é um tipo especial de loop feito para percorrer elementos de uma coleção. Antes, vimos exemplos usando um while e um contador para percorrer uma lista.
# O for elimina a necessidade de inicializarmos um contador, incrementarmos e verificar a condição de parada. Sintaxe:
# for (variável temporária) in (lista):
#  instruções...

# Criando uma lista e fazendo um for, ou seja, pecorrendo a lista:
nomes_cidade = ['São Paulo', 'Londres', 'Tóquio', 'Paris']
for cidades in nomes_cidade:
    print(f'- {cidades}')


# In[2]:


#criando uma lista com a numeração de cada elemento nela:
for numeros in enumerate(nomes_cidade):
    print(f'{numeros}')


# In[3]:


# Usando for em dicionários:
# Criando um dicionário:
cidade = {
    'estado': 'São Paulo',
    'cidade': 'São Paulo',
    'população_milhoes': 12.2
}


# In[4]:


# chave acessa somente a chave estado, cidade e população_milhoes:
for chave in cidade:
    print(f'{chave}: {cidade[chave]}')


# In[5]:


# Função range(), cria uma lista começando do 0 até o elemento indicado -1:
print(list(range(10)))
print((list(range(2, 10))))

#Podemos especificar o valor inicial, o final e o incremento:
print(list(range(2, 10, 2)))


# In[ ]:




