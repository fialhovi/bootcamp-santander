#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Criando uma Lista:
nomes_paises = ['Brasil', 'Argentina', 'China', 'Canadá', 'Japão']

print(f'Tamanho da lista: {len(nomes_paises)} países cadastrados: {nomes_paises}')


# In[5]:


# Indexzação base 0:
print(f'O país no índice 4 é : {nomes_paises[4]}')


# In[6]:


# ou
print(f'O país no índice -1 é : {nomes_paises[-1]}')


# In[7]:


# Trocando o país Japão por Colômbia:
nomes_paises[4] = 'Colômbia'
print(nomes_paises)


# In[8]:


# Retornando os países na posição 1 e 2:
print(f'Retornando os países na posição 1 e 2: {nomes_paises[1:3]}')


# In[9]:


# Retornando os países na posição 1 até a -1:
print(f'Retornando os países na posição 1 até a -1: {nomes_paises[1:-1]}')


# In[10]:


# Retornando os países na posição 2 até o final da minha lista:
print(f'Retornando os países na posição 2 até o final da minha lista: {nomes_paises[2:]}')


# In[11]:


# Retornando os países na posição inicial  até a posição 3:
print(f'Retornando os países na posição inicial  até a posição 3: {nomes_paises[:3]}')


# In[12]:


# Retornando os países pulando de duas em duas posições:
print(f'Retornando os países pulando de duas em duas posições: {nomes_paises[::2]}')


# In[13]:


# Invertendo a ordem da lista:
print(f'Invertendo a ordem da lista: {nomes_paises[::-1]}')


# In[14]:


# Checando se um país está na lista: Retorno boolean:
print('Checando se o país Brasil está na lista: Retorno boolean:', 'Brasil' in nomes_paises)
print()


# In[15]:


# Criando uma nova lista vazia:
lista_capitais = []
print('Criando uma nova lista vazia e Adicionando capitais na minha lista vazia:')


# In[16]:


# Adicionando elementos na minha lista vazia:
lista_capitais.append('Brasília')
lista_capitais.append('Buenos Aires')
lista_capitais.append('Pequim')
lista_capitais.append('Bogotá')

print(lista_capitais)


# In[17]:


# Adicionando um elemento na minha lista em uma posição específica. Ex: Paris na posição 2:
print(f"Adicionando um elemento na minha lista em uma posição específica. Ex: Paris na posição 2: {lista_capitais.insert(2, 'Paris')}")
print(lista_capitais)


# In[18]:


# Removendo um país da lista. No ex: Buenos Aires. Removendo pelo nome:
lista_capitais.remove('Buenos Aires')
print(f'Removendo a capital Buenos Aires: {lista_capitais}')


# In[23]:


# Método pop que remove pela posição do elemento:
removido = lista_capitais.pop(2)
print(f'Removendo a capital {removido} na posição 2: {lista_capitais}')
print()


# In[24]:


# Criando uma lista vazia.
listavazia = []


# In[25]:


# Criando uma lista com alguns valores.
numeros = [1, 3, 7, 8, 9]


# In[26]:


# Listas podem mesclar diferentes tipos de valores.
listamista = [14, "let's code", 0.1, True]


# In[27]:


# Acessamos cada elemento da lista através de um índice entre colchetes.
# Os índices começam em 0.
print(numeros[0])
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])


# In[28]:


# Listas são mutáveis: podemos alterar o valor de seus itens.
numeros[2] = 5
print(numeros)


# In[29]:


# Um jeito inteligente de trabalhar com listas é utilizando loops.
indice = 0
while indice < 5:
    print(f'Um jeito inteligente de trabalhar com listas é utilizando loops: {numeros[indice]}')
    indice = indice + 1

print()
print()


# In[30]:


#Outra função útil é lista.append(), que coloca um elemento novo ao final da lista.
animais = []
resposta = 's'
while resposta == 's' or resposta == 'S':
    resposta = input('Deseja adicionar um animal à lista (s/n)? ')
    if (resposta in 'sS'):
        animal = input('Digite o nome do animal: ')
        animais.append(animal) # adiciona o novo animal à lista
print(animais)
print()
print()


# In[31]:


# A função lista.remove() deleta um elemento da lista. (mas dá erro se o elemento não existir).
animal = input('Digite o animal a ser deletado da lista: ')
animais.remove(animal)
print(animais)
print()
print()


# In[32]:


# Algumas outras funções úteis:

# lista.count() conta quantas vezes um elemento aparece.
jogadores = ['Ronaldo', 'Rivaldo', 'Ronaldo', 'Adriano']
ronaldos = jogadores.count('Ronaldo')
print(jogadores)
print('Quantidade de Ronaldos: ', ronaldos)
print()


# In[33]:


# lista.index() busca em um elemento e fala em qual posição ele aparece.
rivaldo = jogadores.index('Rivaldo')
print("Rivaldo está na posição ", rivaldo)
print()


# In[34]:


# lista.sort() ordena uma lista.
jogadores.sort()
print("jogadores em ordem alfabética: ", jogadores)
print()


# In[35]:


# As funções max(lista) e min(lista) obtém, respectivamente, o maior e o menor valor.
digitos = [3, 1, 4, 1, 5, 9, 2, 6, 5]
maior = max(digitos)
menor = min(digitos)
print(digitos)
print("Maior = ", maior, "e menor = ", menor)
print()
print()


# In[36]:


# Criando uma Tupla:
nome_estado = 'São Paulo', 'Ceará', 'Rio de Janeiro', 'Rio Grande do Sul'
print(f'Tamanho da tupla: {len(nome_estado)} posições.')


# In[37]:


# Atribuindo cada elemento da tupla a uma variavel:
s, c, r, rio = nome_estado
print(s, c,)


# In[38]:


# Uma tupla é uma coleção de objetos que lembra muito as listas.

# Em vez de colchetes, usamos parênteses para declarar as tuplas:
numeros = (1,2,3,5,7,11)


# In[39]:


# Podemos declarar sem parênteses também:
numeros_sem_parenteses = 1, 2, 3, 5, 7, 11


# In[40]:


# Para acessar um valor, utilizamos a mesma sintaxe das listas:
print(numeros[4])
print(type(numeros))


# In[41]:


#Porém, tuplas são imutáveis: não é possível adicionar ou modificar valores.
#Descomentar a linha abaixo provocará erro de execução:

# numeros[4] = 8

# Podemos gerar uma tupla a partir de uma lista...
lista1 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
tupla1 = tuple(lista1)
print(tupla1)


# In[42]:


# ...ou uma lista a partir de uma tupla:
tupla2 = [1, 6, 1, 8]
lista2 = list(tupla2)
print(lista2)


# In[43]:


# Também podemos usar o unpacking com uma tupla:
a, b, c, d, e, f = numeros # "desempacota" a tupla numeros
print("O primeiro vale:", a, "e o ultimo vale:", f)


# In[44]:


#Para ver todos os itens:
print(*nomes_paises)


# In[ ]:




