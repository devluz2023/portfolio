# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:13:25 2019

@author: ecorrea
"""

#P10: Índexação hierárquica
import pandas as pd

moedas  = ['Peso', 'Real', 'Euro', 'Euro', 'Libra']
paises = [['América','América','Europa','Europa','Europa'],
          ['AR','BR','FR','IT','UK']]


paises = pd.Series(moedas, index=paises)

print(paises)                    #imprime toda a Series
print('----------------------') 
print(paises['América'])         #{AR: Peso, BR:Real}
print('----------------------') 
print(paises[:,'IT'])            #{Europa: Euro}
print('----------------------') 
print(paises['Europa','IT'])     #Euro