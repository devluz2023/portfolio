# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:42:41 2019

@author: ecorrea
"""

#P48: Método `reset_index()` 
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-Seleciona apenas as linhas dos países da oceania 
#  com área acima de 200 mil quilômetros quadrados
v =(flags['landmass'] ==6) & (flags['area'] >200)
df = flags[v]

#3-Projeta apenas as colunas "name", "colours", "language", 
#  "landmass" e "area"
df = df[['name','colours','language','landmass','area']]

#4-reseta os índices
df = df.reset_index(drop=True)

#5-Imprime o resultado
print(df)