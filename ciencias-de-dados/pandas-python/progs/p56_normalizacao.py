# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:14:05 2019

@author: ecorrea
"""

#P56: Normalização
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-normaliza a área
area_max = max(flags['area'])
area_min = min(flags['area'])
flags['area_norm'] = (flags['area'] - area_min) / (area_max - area_min)

#3-Imprime o DataFrame alterado
print(flags[['name',
             'area',
             'area_norm']])
