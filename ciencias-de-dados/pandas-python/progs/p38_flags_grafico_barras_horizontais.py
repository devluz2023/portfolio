# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:56:40 2019

@author: ecorrea
"""

#P38: Estudando a base de dados flags
#     Gráficos de barras com as frequências das cores
import pandas as pd

#------------------------------------------------------
#(1)-Importa a base de dados
#------------------------------------------------------
flags = pd.read_csv('c:/bases/flags.csv')

#------------------------------------------------------
#(2)-Gera a tabela de frequências
#------------------------------------------------------
df_cores=pd.DataFrame()
for c in flags.columns: 
    if c in ['red','green','blue','gold','white','black','orange']:
        df_cores[c]=flags[c].value_counts()

#------------------------------------------------------
#(3)-Gera os gráficos de barras
#------------------------------------------------------
lst_cores = [['red','beige'],
             ['green','beige'],
             ['blue','beige'],
             ['gold','beige'],
             ['whitesmoke','beige'],
             ['black','beige'],
             ['orange','beige']]

df_cores.plot(kind='barh', 
              subplots=True,
              figsize=(8,25),
              color = lst_cores)