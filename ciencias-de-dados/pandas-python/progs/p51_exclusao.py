# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:57:19 2019

@author: ecorrea
"""

#P51: Exclusão
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-Mantém apenas os países com verde, amarelo,
#  azul e branco na bandeira
flags = flags.loc[(flags['green']==1) & 
                  (flags['gold']==1) & 
                  (flags['blue']==1) &
                  (flags['white']==1)]

#3-Imprime o DataFrame alterado
print(flags[['name',
            'green',
            'gold',
            'blue',
            'white']])