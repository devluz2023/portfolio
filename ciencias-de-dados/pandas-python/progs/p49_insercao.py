# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:45:27 2019

@author: ecorrea
"""

#P49: Inserção 
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-Cria um DataFrame com os dados do novo país
df_novo = pd.DataFrame(
        {
        'name': 'East Timor',
        'landmass': 5,
        'area': 15,
        'language': 10,
        }, index=[0])

#3-Insere o novo país em flags
flags = pd.concat([flags,df_novo], ignore_index=True, sort=False)

#flags.at[194,'religion']=0

#4-Imprime o DataFrame alterado
print(flags[['name',
            'landmass',
            'area',
            'language',
            'religion'
            ]])