#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Estrutura de repetição while:
contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        print(contador, "Item limpo")
    else: 
        print(contador, "Itens limpos")

print("Fim da repetição do bloco while")


# In[2]:


# while True ou seja laço infinito com parada forçada break:
contador = 0

while True:
    if contador < 10:
        contador = contador + 1
        if contador == 1:
            print(contador, "Item limpo")
        else: 
            print(contador, "Itens limpos")
    else: 
        break
print("Fim da repetição do bloco while")


# In[3]:


# Loop com validação:
texto = input('Digite a sua senha: ')

while texto != 'LetsCode':
    texto = input('Senha inválida. Tente novamente: ')
    
print('Acesso permitido')


# In[4]:


# Utilizando a palavra reservada continue:
contador = 0

while contador < 10:
    contador = contador + 1
    if contador == 1:
        continue
    print(contador, "Itens limpos")

print("Fim da repetição do bloco while")


# In[ ]:




