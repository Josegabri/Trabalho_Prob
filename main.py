import pandas as pd
from statistics import mean, pstdev

data_dado= pd.read_excel('dadosFisicos2023 copy.xlsx', index_col='Mare')
data_dado.drop(['Enchente','Baixamar','Preamar'], inplace=True) 
# A linha de código acima, serve para deixar somente os dados caracterizados como vazantes


# ** MEDIA DAS VARIÁVEIS PEDIDAS  **

data_temperatura= data_dado['T (oC)']
media_temperatura= mean(data_temperatura) # Media da temperatura

data_salinidade= data_dado['S']
media_salinidade= mean(data_salinidade) # Media da Salinidade

data_u= data_dado['u(cm/s)']
media_u = mean (data_u) # Media do componente de velocidade u

data_v= data_dado['v(cm/s)']
media_v= mean(data_v) # Media do componente de velocidade v

print(f'{media_temperatura:.2f}')
print(f'{media_salinidade:.2f}')
print(f'{media_u:.2f}')
print(f'{media_v:.2f}')

# ** DESVIO PADRÃO DAS VARIÁVEIS PEDIDAS **

desvio_temperatura= pstdev(data_temperatura) # Desvio padrão da temperatura

desvio_salinidade= pstdev(data_salinidade) # Desvio padrão da salinidade

desvio_u= pstdev(data_u) # Desvio padrão do componente de velocidade u

desvio_v= pstdev(data_v) # Devio padrão do componente de velocidade v

print (f'\n{desvio_salinidade:.2f}')
print (f'{desvio_temperatura:.2f}')
print (f'{desvio_v:.2f}')
print (f'{desvio_u:.2f}')

# ** CRIAÇÃO DA TABELA **

variavel_temperatura= pd.Series({'Variável': 'Temperatura', 'Média': 21.43,
                                 'Desvio Padrão': 0.84}) 

variavel_salinidade= pd.Series({'Variável':'Salinidade', 'Média': -2.78,
                                'Desvio Padrão':0.19})

variavel_u= pd.Series({'Variável':'u(cm/s)', 'Média':13.93,
                      'Desvio Padrão':4.17})

variavel_v= pd.Series({'Variável':'v(cm/s)', 'Média':-2.78,
                      'Desvio Padrão':9.47})

tabela= pd.DataFrame([variavel_temperatura,variavel_salinidade,variavel_u,variavel_v])
print(tabela)