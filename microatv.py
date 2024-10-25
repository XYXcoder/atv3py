Microatividade 1: Ler um arquivo CSV
python
import pandas as pd
# Leia o arquivo CSV
data = pd.read_csv('seu_arquivo.csv', sep=';', engine='python')
# Exiba os dados
print(data)
Microatividade 2: Criar um subconjunto de dados
python
# Crie um subconjunto de dados
subset = data[['Duration', 'Calories', 'Pulse']]
# Exiba o subconjunto
print(subset)
Microatividade 3: Configurar o número máximo de linhas a serem exibidas
python
# Configurar o número máximo de linhas a serem exibidas
pd.set_option('display.max_rows', 9999)
# Exiba o conjunto de dados
print(data.to_string())
Microatividade 4: Exibir as primeiras e últimas N linhas
python
# Primeiras 10 linhas
print(data.head(10))
# Últimas 10 linhas
print(data.tail(10))
Microatividade 5: Informações gerais sobre o conjunto de dados
python
# Informações gerais sobre o conjunto de dados
print(data.info())
