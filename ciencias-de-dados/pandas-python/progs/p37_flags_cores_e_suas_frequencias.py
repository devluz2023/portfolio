# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:55:35 2019

@author: ecorrea
"""

#P37: Estudando a base de dados flags
#     II. Cores e suas frequências nas bandeiras
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

print(df_cores)
