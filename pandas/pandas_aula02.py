import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

df_concurso = pd.read_csv('dados_concurso.csv')
print(df_concurso.head(), '\n')

'''Quantas pessoas são do estado do Piauí?'''
print(df_concurso[df_concurso['Estado']=='PI']['Número de Inscrição'].count(), '\n')
print(df_concurso[['Número de Inscrição', 'Estado']].groupby('Estado').count(), '\n') 

'''Qual a distribuição de escolaridade por estado?'''
print(df_concurso[['Estado', 'Escolaridade', 'Número de Inscrição']].groupby(['Estado', 'Escolaridade']).count(), '\n') 

'''Qual é a porcentagem de pessoas com deficiência?'''
print(df_concurso['Deficiência'].value_counts(normalize=True)*100, '\n')

'''Qual a média de idade por região?'''

'''Quantas do ES são do sexo feminino?'''

'''Retorne o dado com número de inscrição, nome e data de nascimento'''
print(df_concurso[['Número de Inscrição', 'Data de Nascimento', 'Nome']], '\n')

'''Quantas pessoas nasceram antes de 1995?'''
df_concurso['Data de Nascimento'] = pd.to_datetime(df_concurso['Data de Nascimento'])
print(df_concurso.loc[df_concurso['Data de Nascimento'] < np.datetime64('1994')], '\n')

'''Quais foram os 10 primeiros inscritos?'''
print(df_concurso.set_index('Data de Inscrição').sort_index()[:10], '\n')
print(df_concurso.sort_values('Data de Inscrição').iloc[:10, :], '\n')

'''Plote a porcentagem de dados faltosos para cada coluna'''
print(df_concurso.isna().sum().plot(kind='bar'), '\n')
plt.show()

'''Para os valores faltosos coloque:'''
#se string: falta informação
#se número: mediana
#df_concurso.isna()
df_concurso = df_concurso.fillna('Falta Informação')
print(df_concurso, '\n')
print(df_concurso['Estado'].unique(), '\n')
