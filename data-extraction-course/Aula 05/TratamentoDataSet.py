arquivo = "data\\voos_2025_1.csv"

import pandas as pd

df = pd.read_csv(arquivo, sep=';', encoding='utf-8', skiprows=1)

#tirar dupliocadas
df = df.drop_duplicates()

#colunas do dataset
df.columns

#colunas que não podem ter nulos
colunas_criticas = [
    'ICAO Aeródromo Destino', 
    'ICAO Aeródromo Origem', 
    'Partida Prevista', 
    'Partida Real', 
    'Chegada Prevista', 
    'Chegada Real',
    'Situação Voo'
]

df_limpo = df.dropna(subset=colunas_criticas)

#estudando coluna Codigo justificativa 
df['Código Justificativa'].unique()


#analisando tabelas Codigo tipo linha 
df['Código Tipo Linha'].unique()

df_limpo = df[df['Código Tipo Linha'].isin(['N', 'I']).copy()]

# 3. Verifica se funcionou (Profiling)
print(df_limpo['Código Tipo Linha'].unique())
#estudando coluna Codigo autorizacao(Di)
df['Código Autorização (DI)'].unique()
df_limpo = df[df['Código Autorização (DI)'] != '0']

#criando dicionario
dict_index = df_limpo.to_dict(orient='index')
dict_colunas = df_limpo.to_dict(orient='list')



