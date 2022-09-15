#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Um arquivo CSV tem valores separados por vírgulas, normalmente vêm de planilhas.
# Importando um biblioteca:
import csv


# In[3]:


# Criando um leitor específico para ler cada uma das linhas do CSV.
# Passando o path() para uma variável e fazendo um 'for' para ler linha por linha. Os valores são separados por vírgula, e o retorno de cada valor é uma lista.
with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor)
    for linha in leitor:
            print(linha)


# In[5]:


## Mostrando os valores apenas quando 'novos_casos', ou seja, na posição 2 da lista for maior que 1:
with open('brasil_covid.csv', 'r', encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    header = next(leitor)
#A função 'next' pula o header, o cabeçalho, nesse caso.
    for linha in leitor:
        if float(linha[2]) > 1:
            print(linha)


# In[6]:


# Fazendo a mesma leitura do arquivo sem importar a biblioteca csv:
with open('brasil_covid.csv', 'r', encoding='utf-8') as csv_file:
    linhas = csv_file.read()
    linhas = linhas.split('\n')
    for linha in linhas:
        linha = linha.split(',')
        print(linha)


# In[7]:


# Criando um arquivo CSV.
# Temos que criar um escritor específico para o tipo de arquivo CSV.
# Com a função 'writerow', escrevemos uma linha:
with open('users.csv', 'w', encoding='utf-8', newline='') as arquivo_users:
    escritor = csv.writer(arquivo_users)
    escritor.writerow(['nome', 'sobrenome', 'email', 'gênero'])
    escritor.writerow(['Vinícius', 'Fialho', 'fialhov@hotmail.com', 'Masculino'])


# In[8]:


# No entanto, a cada linha criada, o Python colocou uma linha no final, separando-as. Por isso, acrescentamos newline=''.


# In[9]:


# Para facilitar o preenchimento, o professor passou o seguinte código.
header = ['nome', 'sobrenome', 'email', 'genero']
dados = []
opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
while opt != '0':
    nome = input("Qual o seu nome? ")
    sobrenome = input("Qual o seu sobrenome? ")
    email = input("Qual o seu email? ")
    genero = input("Qual o seu gênero? ")
    dados.append([nome,sobrenome,email,genero])
    opt = input('O que deseja fazer?\n1 - Cadastrar\n0 - Sair\n')
print(dados)

with open('users.csv', 'w', newline='') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    writer.writerow(header)
    writer.writerows(dados)
    
with open('users.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        print(row)


# In[ ]:




