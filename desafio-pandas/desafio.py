import sys
sys.path.append(r'c:\users\user\appdata\local\programs\python\python310\lib\site-packages')

import pandas as pd
import numpy as np

# Carregando os dados
dados = pd.read_csv('saude_do_sono_estilo_vida.csv')

# Renomeando as colunas
dados.rename(columns={'ID': 'Identificador',
                      'Pressão sanguíneaaaa': 'Pressão sanguínea',
                      'Ocupação': 'Profissão',
                      'Categoria BMI': 'Categoria IMC'}, inplace=True)
print("1. Renomeando as colunas:")
print(dados.columns.tolist(), "\n")

# 2. Média, moda e mediana de Duração do sono para cada profissão
estatisticas_sono = dados.groupby('Profissão')['Duração do sono'].agg(['mean', np.median, pd.Series.mode])
print("\n2. Média, moda e mediana de Duração do sono para cada profissão:")
print(estatisticas_sono)

# 3. Porcentagem de obesidade entre engenheiros de software
porcentagem_obesidade_eng_soft = (dados[dados['Profissão'] == 'Eng. de Software']['Categoria IMC'].value_counts(normalize=True)['Obesidade'] * 100)
print("\n3. Porcentagem de obesidade entre engenheiros de software:")
print(f"{porcentagem_obesidade_eng_soft:.2f}%")

# 4. Comparando média de Duração do sono entre advogados/representantes de vendas
media_sono_advogados = dados[dados['Profissão'].isin(['Advogado', 'Representante de Vendas'])].groupby('Profissão')['Duração do sono'].mean()
print("\n4. Comparando média de Duração do sono entre advogados e representantes de vendas:")
print(media_sono_advogados)

# 5. Comparando média de Duração do sono entre enfermeiros e médicos
media_sono_enf_med = dados[dados['Profissão'].isin(['Enfermagem', 'Medicina'])].groupby('Profissão')['Duração do sono'].mean()
print("\n5. Comparando média de Duração do sono entre enfermeiros e médicos:")
print(media_sono_enf_med)

# 6. Subconjunto de colunas específicas
subconjunto = dados[['Identificador', 'Gênero', 'Idade', 'Pressão sanguínea', 'Frequência cardíaca']]
print("\n6. Subconjunto de colunas específicas:")
print(subconjunto)

# 7. Profissão menos frequente
profissao_menos_frequente = dados['Profissão'].value_counts().idxmin()
print("\n7. Profissão menos frequente:")
print(profissao_menos_frequente)

# 8. Calcular a média da pressão sanguínea por gênero
# Função para extrair a média da pressão sistólica e diastólica
def calcular_media_pressao_sanguinea(pressao):
    valores = [int(valor) for valor in pressao.split('/')]
    media = np.mean(valores)
    return media

# Aplicar a função à coluna 'Pressão sanguínea'
dados['Média_pressão_sanguínea'] = dados['Pressão sanguínea'].apply(calcular_media_pressao_sanguinea)

media_pressao_sanguinea_genero = dados.groupby('Gênero')['Média_pressão_sanguínea'].mean()
print("\n8. Média de pressão sanguínea por gênero:")
print(media_pressao_sanguinea_genero)

# 9. Predominância de dormir 8 horas por dia (usando moda)
predominancia_8_horas = (dados['Duração do sono'].mode()[0] == 8)
print("\n9. Predominância de dormir 8 horas por dia:")
print(predominancia_8_horas)

# 10. Comparando média de passos entre frequências cardíacas
# Filtrar os dados antes de calcular a média dos passos
dados_filtrados = dados[dados['Frequência cardíaca'] > 70]
media_passos_freq_cardiaca = dados_filtrados['Passos diários'].mean()
print("\n10. Comparando média de passos entre frequências cardíacas:")
print(media_passos_freq_cardiaca)
