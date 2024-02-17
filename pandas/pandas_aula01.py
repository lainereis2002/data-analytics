import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import pandas as pd
df = pd.read_csv('carros.csv')

'''1. Print seu head com 10 linhas'''
print(df.head(10), "\n")

'''2. agora print as colunas e index do dataframe'''
print(df.columns, "\n")
print(df.index, "\n")

'''3. faça um sort decrescente no dataframe pelo estado com maior quantidade de carros'''
print(df.sort_values('Quant Carros', ascending=False), "\n")

'''4. descubra qual a proporção de carro para a população de 
cada estado e insira em uma nova coluna'''
proporcao = df['Quant Carros']/df['População do Estado']
#print(proporcao, "\n")
df['Carros por habitante'] = proporcao
print(df.head(), "\n")

'''5. faça um dataframe com estado e proporção de carro por habitante'''
df_estado_hab = df[['Estado', 'Carros por habitante']]
print(df_estado_hab, "\n")