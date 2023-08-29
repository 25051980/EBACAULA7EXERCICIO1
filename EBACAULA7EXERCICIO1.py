#!/usr/bin/env python
# coding: utf-8

# # Módulo 07, Tarefa 01
# 
# Vamos começar a mexer na nossa base de projeto? Já fizemos um exercício de montar a variável resposta, já pudemos perceber que essa atividade pode não ser trivial. Vamos agora trabalhar a base para que fique propícia ao *scikitlearn* para trabalharmos.
# 
# Lembrando, a base se chama demo01.csv, e originalmente está publicada [aqui](https://www.kaggle.com/rikdifos/credit-card-approval-prediction).

# #### 1) Carregue a base e avalie:
# 
# - As variáveis
# - Tipos de dados de cada variável
# - Quantidade de missings
# - Distribuição da variável resposta (mau)

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt

# Carregar a base de dados
data = pd.read_csv('credit_record.csv')  # Substitua pelo caminho correto do arquivo

# Variável escolhida para análise
variavel_escolhida = 'STATUS'

# Visualizar as primeiras linhas do DataFrame
print(data.head())

# Verificar os tipos de dados de cada variável
print(data.dtypes)

# Verificar quantidade de valores ausentes (missings) por variável
missing_count = data.isnull().sum()
print(missing_count)

# Plotar a distribuição da variável escolhida
plt.figure(figsize=(8, 6))
data[variavel_escolhida].value_counts().plot(kind='bar')
plt.title(f'Distribuição da Variável {variavel_escolhida}')
plt.xlabel(variavel_escolhida)
plt.ylabel('Contagem')
plt.show()



# #### 2) Vamos montar um metadados
# 
# 1. Crie um dataframe com os nomes de cada variável e o tipo de dados de cada variável.
# 2. Adicione uma coluna nesse *dataframe* chamada "qtd_categorias" e coloque nela o número de categorias correspondente de cada variável. 
#     Dica: 
#         1. inicie uma lista vazia
#         2. faça um for ao longo dos nomes das variáveis, 
#         3. conte o número de categorias dessa variável 
#         4. acumule essa informação de 3. na lista que você criou em 1. 
#         5. No final, essa lista pode ser atribuída à nossa variável.
# 3. Crie variáveis dummy para as variáveis necessárias (i.e. aquelas que são qualitativas e não estão armazenadas como {0, 1} ou {True, False}.

# In[ ]:





# #### 3) Crie variáveis dummy para as variáveis necessárias (i.e. aquelas que são qualitativas e não estão armazenadas como {0, 1} ou {True, False}. Crie um *dataframe* apenas com as variáveis apropriadas para entrada no scikitlearn - elimine as variáveis tipo *str*, mantendo apenas suas versões *dummy*.

# In[ ]:





# #### 4) Qual variável é mais poderosa?
# 
# Considere as variáveis ```possui_email``` e ```posse_de_veiculo```. Faça uma tabela cruzada entre elas e responda qual delas te parece mais poderosa para prever a probabilidade de ```mau = 1```?

# In[ ]:





# #### 5) Salve a base, pois ela será utilizada no final deste módulo.

# In[ ]:




