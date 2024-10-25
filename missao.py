# 1. Leia o CSV
data = pd.read_csv('seu_arquivo.csv', sep=';', engine='python')

# 2. Exiba informações gerais
print(data.info())
print(data.head())
print(data.tail())

# 3. Crie uma cópia do conjunto de dados
data_cleaned = data.copy()

# 4. Substitua valores nulos na coluna 'Calories'
data_cleaned['Calories'].fillna(0, inplace=True)
print(data_cleaned)

# 5. Substitua valores nulos na coluna 'Date'
data_cleaned['Date'].fillna('1900/01/01', inplace=True)
print(data_cleaned)

# 6. Transforme a coluna 'Date' em datetime
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'], errors='coerce')

# 7. Substitua '1900/01/01' por NaN e transforme novamente
data_cleaned['Date'].replace('1900/01/01', pd.NaT, inplace=True)

# 8. Resolva o erro da data "20201226"
data_cleaned['Date'] = data_cleaned['Date'].replace('NaT', pd.NaT)  # mantendo NaT
data_cleaned.loc[data_cleaned['Date'].isna(), 'Date'] = pd.to_datetime('2020-12-26')

# 9. Transforme novamente
data_cleaned['Date'] = pd.to_datetime(data_cleaned['Date'], errors='coerce')

# 10. Remova registros com valores nulos
data_cleaned.dropna(inplace=True)

# 11. Exiba o dataframe final
print(data_cleaned)
