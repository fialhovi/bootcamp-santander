#!/usr/bin/env python
# coding: utf-8

# In[1]:


#P/ começar, importar a biblioteca 'request', dando o apelido 'r', para facilitar a referenciação:
import requests as r


# In[2]:


#Chamando a bilbioteca para essa url:
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url)


# In[3]:


#Vamos ver o status dessa requisição para ver se deu tudo certo:
resp.status_code


# In[4]:


#guardar os dados na variável raw data:
raw_data = resp.json()


# In[5]:


#Vamos ver o que tem lá na raw_data, pegar a posição 0 já que é uma lista com essas informações:
raw_data[0]


# In[6]:


#Para o nosso objetivo, tem algumas coisas que não precisamos armazenar (ex. país, código do país, latitude etc.)
#Vamos filtrar apenas as informações que vamos precisar:
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'],obs['Deaths'],obs['Recovered'],obs['Active'],obs['Date']])


# In[7]:


#Vamos adicionar os headers, para identificar o que é cada item:
final_data.insert(0, ['Confirmados', 'Obitos', 'Recuperados', 'Ativos', 'Data'])
final_data


# In[8]:


#Vamos criar variáveis que serão constantes para a limpeza dos dados.
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4


# In[9]:


#Agora, vamos sobrescrever algumas 'obs' que temos em final_data, então vamos pegar as posições.
#Aqui, retirando os minutos, horas e segundos da data, que não importam para a nossa análise:
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10]
final_data


# In[10]:


#Vamos transformar a string de data para o tipo Data de verdade:
import datetime as dt


# In[11]:


# DateTime: Data, hora, segundo e microsegundo:
print(dt.time(12, 6, 21, 7), 'Hora:minuto:segundo:microsegundo')
print('----')
print(dt.date(2021, 10, 30), 'Ano/mês/dia')
print('----')
print(dt.datetime(2021, 10, 30, 12, 6, 21, 7), 'Ano/mês/dia Hora:minuto:segundo:microsegundo')


# In[12]:


# Tipos de datas contadores de segundos:

natal = dt.date(2021, 12, 25)
reveillon = dt.date(2022, 1, 1)
print({reveillon - natal})
print(f'Faltam {(reveillon - natal).days} dias para o reveillon')
print(f'Faltam {(reveillon - natal).total_seconds()} segundos para o reveillon')
print(f'Faltam {(reveillon - natal).microseconds} microsegundos para o reveillon')


# In[13]:


# Transformando os dados da minha API em csv:
import csv


# In[14]:


with open('brasil-covid.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(final_data)


# In[15]:


# Alterando a data dos dados que é string para datetime:
for i in range(1, len(final_data)):
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')


# In[16]:


final_data


# In[17]:


# Criando uma função para construir os dados do eixo y:
def get_datasets(y, labels):
    if type(y[0]) == list:
        datasets = []
        for i in range(len(y)):
            datasets.append({
                'label': labels[i],
                'data': y[i]
                })
        return datasets
    else:
        return [
            {
                'label':labels[0],
                'data': y
            }
        ]


# In[18]:


# Função para definir o titulo do gráfico:
def set_title(title=''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }


# In[19]:


# Função que cria o nosso dicionário, que cria o gráfico:
def create_chart(x, y, labels, kind='bar', title=''):
    
    datasets = get_datasets(y, labels)
    options = set_title(title)
    
    chart = {
        'type' : kind,
        'data' : {
            'labels': x,
            'datasets' : datasets
        },
        'options' : options
    }
    
    return chart


# In[20]:


# Função para fazer a requisição na API: o retorno é binário
def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content


# In[21]:


# Função para salvar a imagem:
def save_image(path, content):
    with open(path, 'wb') as image:
        #o 'wb' indica que é uma escrita binária.
        image.write(content)


# In[22]:


#Importar bibliotecas e suas funções:
get_ipython().system('pip install Pillow')

from PIL import Image
from IPython.display import display


# In[23]:


# Função para mostrar a imagem
def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


# In[29]:


y_data_1 = []
for obs in final_data[1::30]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_data[1::30]:
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['Confirmados', 'Recuperados']

x = []
for obs in final_data[1::30]:
    x.append(obs[DATA].strftime('%d/%m/%Y'))
    
chart = create_chart(x, [y_data_1, y_data_2], labels, title='Gráfico confirmados vs recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
display_image('meu-primeiro-grafico.png')


# In[30]:


#importar mais função para gerarmos um qr code para o nosso gráfico:
from urllib.parse import quote


# In[31]:


# Gerar QR-CODE:
def get_api_qrcode(link):
    text = quote(link) # parsing do link para url
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content


# In[32]:


# Recuperar o link
url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
display_image('qr-code.png')


# In[ ]:




