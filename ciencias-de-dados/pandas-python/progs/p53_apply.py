# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:03:36 2019

@author: ecorrea
"""

#P53: Método apply()
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-apply
flags['name'] = flags['name'].apply(str.upper)

#3-Imprime o DataFrame alterado
print(flags)