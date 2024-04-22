# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:00:41 2019

@author: ecorrea
"""

#P52: Método replace()
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-replace
flags['green'] = flags['green'].replace([0,1],['Não','Sim'])

#3-Imprime o DataFrame alterado
print(flags[['name','green']])