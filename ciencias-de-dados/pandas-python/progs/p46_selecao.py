# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:34:30 2019

@author: ecorrea
"""

#P46: Seleção 
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-Seleciona apenas as linhas dos países da oceania
v = (flags['landmass']==6)
flags_oceania = flags[v]

#3-imprime os países da oceania
print(flags_oceania)

print(flags[v])

"""
v = (flags['language'] ==1) | (flags['language'] ==4)
v = (flags['landmass']!=6) 
v = (flags['colours'] <=2) 
v = (flags['landmass'] ==6) & (flags['area'] >200)
v = (flags['landmass'] ==6) & (flags['area'] >200) & (flags['language'] ==1)
"""