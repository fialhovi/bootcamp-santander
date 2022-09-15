#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Strings I
empresa = "Let's code"
print(empresa)
print()


# In[4]:


#Usando o caractere de escape \ para não dar conflito
frase = "O Professor Pietro da Let's Code disse: \"Hoje a pizza é por minha conta\""
print(frase)
print()


# In[5]:


#Método len():
tamanho = len(frase)
print("A frase possui", tamanho, "caracteres")


# In[6]:


# Fatiando uma String:
empresa1 = 'Google'
print(f'Mostrando a letra na posição 0 do nome {empresa1}: {empresa1[0]}')


# In[7]:


print(f'Mostrando as três primeiras letras do nome {empresa1}: {empresa1[:3]}')


# In[8]:


# Método split para String's:
nomes_cidades = 'São Paulo, Belo Horizonte, Rio de Janeiro, Brasilia'
print(nomes_cidades[0]) # Antes do método split(', ') ele retorna somente a primeira letra 's' da cidade de são paulo
nomes_cidades = nomes_cidades.split(', ')
print(nomes_cidades)
print(nomes_cidades[0]) # Usando o método split ele retorna o nome da cidade de São Paulo
print(nomes_cidades[1])
print()


# In[9]:


# Método strip():
cabecalho = '               MENU PRINCIPAL          '


# In[10]:


# Sem o método strip():
print(f'Sem o método strip(): {cabecalho}')


# In[11]:


# Com o método strip():
print(f'Com o método strip(): {cabecalho.strip()}')
print()


# In[12]:


# Métodos: title(), capitalize(), lower(), upper():
cidade = 'rIo dE JaNeiRo'
print(f'Usando o Método title(): {cidade.title()}')
print(f'Usando o Método capitalize(): {cidade.capitalize()}')
print(f'Usando o Método lower(): {cidade.lower()}')
print(f'Usando o Método upper(): {cidade.upper()}')
print()


# In[13]:


# Exercicio:
nome_cidade = input('Qual cidade do Brasil é conhecida como cidade maravilhosa?  ').strip()
while nome_cidade.lower() != 'rio de janeiro':
    print('Tenta de novo aí...')
    nome_cidade = input('Qual cidade do Brasil é conhecida como cidade maravilhosa?  ').strip()
print('Boa Campeão!! ')


# In[14]:


# Podemos converter strings para listas:
listafrase = list(frase)
print(f'Podemos converter strings para listas: {listafrase}')


# In[15]:


# A função join() intercala cada elemento de uma lista com uma string.
stringfinal = '-py'.join(listafrase)
print(stringfinal)
print()


# In[16]:


# Usar um join() com uma string vazia é útil para transformar a lista de volta
# em string:
stringfinal = ''.join(listafrase)
print(stringfinal)


# In[17]:


# Podemos inserir quebras de linha com '\n'
frase = 'uma\nFRASE'
print(frase)


# In[18]:


# Podemos inserir tabulação com '\t'
frase = 'uma\n\tFRASE'
print(frase)


# In[19]:


# Para conseguir representar a barra '\', precisamos de 2 barras:
frase = 'uma\\FRASE'


# In[20]:


print(frase)


# In[ ]:




