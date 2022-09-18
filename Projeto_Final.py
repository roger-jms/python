import requests as r
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url) #requisição

# indicar a url da API
url = 'https://api.covid19api.com/dayone/country/brazil'
resp = r.get(url) #requisição

# testar se a requisição foi bem sucedida
resp.status_code
raw_data = resp.json() # armazenar o retorno da requisição
raw_data[0] #verificar o que tem na linha 1
raw_data = resp.json() # armazenar o retorno da requisição
raw_data[0] #verificar o que tem na linha 1
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])

# filtrar as informações que queremos
final_data = []
for obs in raw_data:
    final_data.append([obs['Confirmed'], obs['Deaths'], obs['Recovered'], obs['Active'], obs['Date']])
final_data.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])
final_data.insert(0, ['Confirmados', 'Óbitos', 'Recuperados', 'Ativos', 'Data'])
final_data

# criando constantes para referenciar as informações dentro da lista
CONFIRMADOS = 0
OBITOS = 1
RECUPERADOS = 2
ATIVOS = 3
DATA = 4
final_data[i][DATA] = final_data[i][DATA][:10]

# realizando a limpeza da data, deixando apenas o dia
for i in range(1, len(final_data)):
    final_data[i][DATA] = final_data[i][DATA][:10] #recebe ele mesmo com o slice de 10 posições, 0 a 9
final_data
import datetime as dt # importando a biblioteca datatime: formata em data e hora

# Guardando os dados em CSV
import csv
# Criando arquivo
with open('brasil-covid.csv', 'w') as file: #criando
    writer = csv.writer(file) #usando método para escrita
    writer.writerows(final_data) #escrevendo os dados armazenados em final_data
final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')

# transformando a string representativa de data em data mesmo
for i in range(1, len(final_data)):
    # fazendo a formatação utilizando o datetime
    # informando a posição com o valor da string-data e o formato desejado para a data
    final_data[i][DATA] = dt.datetime.strptime(final_data[i][DATA], '%Y-%m-%d')
final_data

# criando funções de ajuda para uso da API QuickChart
# função para definir os dados do gráfico
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
                'label': labels[0],
                'data': y
            }
        ]
​
# função para definição do título do gráfico
def set_title(title = ''):
    if title != '':
        display = 'true'
    else:
        display = 'false'
    return {
        'title': title,
        'display': display
    }
​
# função que cria o dicionário que representa o gráfico
# recebe as informações solicitadas na API
def create_chart(x, y, labels, kind='bar', title=''):
    datasets = get_datasets(y, labels)
    options = set_title(title)
    
    chart = {
        'type' : kind,
        'data' : {
            'labels': x,
            'datasets': datasets
        },
        'options': options
    }
    return chart
f'{url_base}?c={str(chart)}'
# função para realizar a requisição na API usando o dicionário create_chart
# recebendo um valor binário. Usamos o content para armazenar o valor binário
def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content
conteudo
# função para salvar a imagem recebida em binário
def save_image(path, conteudo):
    with open(path, 'wb') as imagem: # w=escrita e b=binario
        imagem.write(conteudo)
.open
# função para mostar a imagem do gráfico aqui no notebook
from PIL import Image
from IPython.display import display
def mostrar_imagem(path):
    img_pil = Image.open(path)
    display(img_pil)
# programa para criar os dados e gerar o gráfico
​
#dados de y
y_data_1 = []
for obs in final_data[1::100]: #informações a cada 100 dias
    y_data_1.append(obs[CONFIRMADOS])
​
y_data_2 = []
for obs in final_data[1::100]: #informações a cada 100 dias
    y_data_2.append(obs[RECUPERADOS])
    
labels = ['Confirmados', 'Recuperados']
​
x = []
for obs in final_data[1::100]: #informações a cada 100 dias
    x.append(obs[DATA].strftime('%d/%m/%Y'))
    
chart = create_chart(x, [y_data_1, y_data_2], labels, title = 'Gráfico de Casos Confirmados vs Recuperados')
chart_content = get_api_chart(chart)
save_image('meu-primeiro-grafico.png', chart_content)
mostrar_imagem('meu-primeiro-grafico.png')
# função para criar Qrcode do meu primeiro gráfico para ser compartilhado
from urllib.parse import quote
def get_api_qrcode(link):
    text = quote(link) # parsing do link para url
    url_base = 'https://quickchart.io/qr'
    resp = r.get(f'{url_base}?text={text}')
    return resp.content
# criando e mostrando o qrcode
url_base = 'https://quickchart.io/chart'
link = f'{url_base}?c={str(chart)}'
save_image('qr-code.png', get_api_qrcode(link))
mostrar_imagem('qr-code.png')
