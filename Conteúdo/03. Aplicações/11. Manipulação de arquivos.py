#!/usr/bin/env python
# coding: utf-8

# In[1]:


# LER UM ARQUIVO

# Abrir arquivo:
# 1°) criar uma variável que vai receber o retorno do método;
# 2°) método open(), em que passa o parâmetro e o caminho(path) do arquivo, se tiver na mesma pasta do projeto, então é só digitar o nome do arquivo, se não, escrever o nome das pastas para frente até chegar a ele ou escrever para trás, caso esteja em pastas anteriores, ex., ../../exemplo.txt;
# 3°) forma de abertura do arquivo, neste exemplo, utilizaremos o 'r', de leitura.
arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
# fazer a leitura do texto do arquivo:
texto = arquivo.read()
print(texto)
# Toda vez que abrir um arquivo, ele deve ser fechado, para não dar problemas futuros:
arquivo.close()


# In[2]:


#Outra forma de ler o texto, linha a linha, até o seu fim, é utilizando a seguinte função:
arquivo = open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8')
linha = arquivo.readline()
while linha != '':
    print(linha, end='')
    linha = arquivo.readline()
arquivo.close()


# In[3]:


#Também conseguimos abrir o arquivo para leitura utilizando o "for", por exemplo:
arquivo = open('dom_casmurro_cap_1.txt', 'r',encoding='utf-8')
for linha in arquivo:
    print(linha, end='')
arquivo.close()


# In[4]:


#Uma boa forma de fechar o arquivo sem utilizar o ".close()" no final é utilizar a função "with"
# O "as" é para dar um apelido para ele, no caso, apelidamos de 'arquivo':
with open('dom_casmurro_cap_1.txt', 'r', encoding='utf-8') as arquivo:
    texto = arquivo.read()
    print(texto)


# In[5]:


# ESCREVER EM UM ARTIGO

#Criar um arquivo para escrever.
#Nele, utilizamos o modo de abertura 'w', de write, que cria um arquivo novo ou SOBRESCREVE (CUIDADO) o arquivo com esse nome.
#'\n', como vimos, é a quebra de linha.
with open('arquivo_teste.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write('Essa é uma linha que eu escrevi usando Python\n')
    arquivo.write('Essa é a segunda linha que eu escrevi usando Python\n')


# In[6]:


with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')


# In[7]:


#Para adicionar um texto nesse arquivo, usamos o modo de abertura 'a':
with open('arquivo_teste.txt', 'a', encoding='utf-8') as arquivo:
    arquivo.write('Essa é a terceira linha que eu escrevi usando Python\n')


# In[8]:


with open('arquivo_teste.txt', 'r', encoding='utf-8') as arquivo:
    print(arquivo.read(), end='')


# In[9]:


#Há outros modos de abertura que combinam leitura e escrita, como o 'r+', que fornecerá ambos os sets de função.


# In[ ]:




