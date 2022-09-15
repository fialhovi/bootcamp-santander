#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Funções:

# Declarando uma função sem parêmetro:
def hello():
    print('Olá, Mundo!')


hello()


# In[3]:


# Declarando uma função com parâmetro que calcula a média aritmética de três notas:
def calcula_media(valor1, valor2, valor3):
    soma = valor1 + valor2 + valor3
    media = soma / 3
    return media


# In[4]:


nota = calcula_media(8.5, 4.9, 10)
print(f'Média: {nota}')


# In[5]:


# Funções recursivas:

def funcaoRecursiva(numero):
    if (numero != 1):
        funcaoRecursiva(numero - 1)
    print(numero)


# In[6]:


print("Testando a função recursiva:")
funcaoRecursiva(10)


# In[7]:


# Funções II

# Funções com varios parâmetros: quando utilizamos um * em parâmetros, quer dizer que podemos passar vários argumentos, que são armazenados em
# uma tupla().
def calcula_media1(*args):
    soma = sum(args)
    media = soma / len(args)
    return media


# In[8]:


print(f'Média de vários parâmetros: {calcula_media1(10, 5, 8, 9, 10, 7, 6, 2)}')


# In[9]:


# Funções com vários parâmetros: quando utilizamos dois ** em parâmetros, quer dizer que podemos passar vários argumentos, que são armazenados em
# um dicionario().
def print_info(**kwargs):
    print(kwargs, type(kwargs))


# In[10]:


print_info(nome='Vinícius', sobrenome='Fialho')


# In[ ]:




