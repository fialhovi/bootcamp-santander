#!/usr/bin/env python
# coding: utf-8

# In[1]:


# API: Application Programming Interface
# Hoje em dia, é muito comum que diferentes aplicações consumam dados pela internet, muitas vezes dados providenciados por terceiros.
# Por exemplo, um aplicativo de entrega de alimentos pode usar dados de geolocalização do Google para localizar restaurantes próximos ao usuário e exibir a
# rota percorrida pelo entregador. API, nesse curso, é usada para descrever uma interface online que permite a comunicação com dados.
#
# Como as aplicações podem rodar em diferentes plataformas (Windows, Android, MacOS, iOS, um navegador de internet...),
# é importante estabelecer uma linguagem comum para que todos consigam consumir esses dados.
# Essa "linguagem comum" é o que chamamos de API: Application Programming Interface. A organização que disponibiliza os dados estabelece algumas
# "regrinhas" para fazermos requisições, e em contrapartida ela garante que os recursos fornecidos também seguirão certos padrões, facilitando a vida dos
# programadores.
# Portanto, quando decidimos utilizar uma API, a primeira coisa que precisamos fazer é estudar sua documentação. Vejamos alguns dos pontos mais relevantes
# para procurar.
# Todos os exemplos de requisição que mostraremos aqui podem ser colados em seu navegador ou estudados usando um requests.get no Python e imprimindo seu
# campo text.

#O dado retornado pela API é chamado de json. Essa sigla quer dizer javascript object notation.
#Usar o pip (instalador de resquests do Python) para instalar a biblioteca:
get_ipython().system('pip install requests')


# In[2]:


#importar a biblioteca agora:
import requests


# In[3]:


#agora, definir a url que vamos fazer a chamada (nesse caso, vamos utilizar a chamada get):
url = 'https://api.exchangerate-api.com/v6/latest'
# variável req = requests (que é a nossa biblioteca).get (chamada)
req = requests.get(url)
#é importante ver o status da url, porque pode dar o erro de não encontrado. Se retornar 200, está ok.
print(req.status_code)


# In[4]:


# agora, vamos recuperar os dados da requisição
# Recuperando os dados da requisição: o json() retorna um dicionário.
dados = req.json()
print(dados)


# In[5]:


#no valor que retorna, vemos 'base code', que indica a moeda padrão utilizada, no caso, usd, dólar americano.
#aqui, o que queremos é saber um valor em reais sendo convertido para dólar:
valor_reais = float(input('Informe o valor em R$ a ser convertido\n'))
#dados na posição rates com a chave BRL.
cotacao = dados['rates']['BRL']
print(f'R${valor_reais} em dólar valem US$ {(valor_reais / cotacao):.2f}')


# In[6]:


# Consumindo APIs em Python
# As APIs são meios de nos conectarmos a recursos na internet. Portanto, já possuímos as ferramentas na mão desde os capítulos anteriores.
# Você irá construir a lógica para decidir o que você irá buscar/consultar, montará uma string seguindo o formato indicado pela documentação da API (como todos os exemplos deste capítulo). Em seguida você tratará a resposta de acordo:
#
# Se for JSON, utilize o método json da própria requests.
# Se for CSV, utilize o módulo CSV estudado anteriormente.
# Se for XML, podemos utilizar o módulo BeautifulSoup, que não será estudado aqui.
# Para outros formatos, provavelmente a solução mais fácil será baixar um módulo preparado para lidar com eles.
# Descobrindo APIs: tem boas ideias e gostaria de saber se existe uma boa API para ajudar? Confira alguns bons repositórios de API organizados por categoria:
#
# https://github.com/n0shake/public-apis
#
# https://github.com/public-apis/public-apis
#
# https://any-api.com/
#
# Sites de governos costumam ter uma grande riqueza de dados também. Segue abaixo algumas sugestões (oficiais ou mantidas por voluntários) com dados do
# Brasil como um todo. Experimente buscar por bases de dados de sua cidade ou estado!
#
# http://www.transparencia.gov.br/swagger-ui.html
#
# http://www.dados.gov.br/
#
# https://brasil.io/home/


# In[ ]:




