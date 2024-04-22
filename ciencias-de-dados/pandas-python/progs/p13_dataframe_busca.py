# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:21:51 2019

@author: ecorrea
"""

#P13: Busca em DataFrames
import pandas as pd

#cria o DataFrame
dados = {'nome': ['Argentina','Brasil','França','Itália',
                  'Reino Unido'],
         'continente': ['América','América','Europa','Europa',
                        'Europa'],
         'extensao': [2780,8511,644,301,244],
         'corVerde': [0,1,0,1,0]}

siglas = ['AR','BR','FR','IT','UK']

paises = pd.DataFrame(dados,index=siglas)

#testa se um dado rótulo de linha existe
tem_BR = 'BR' in paises.index
tem_US = 'US' in paises.index
print("existe o rótulo 'BR? -> ",tem_BR)        
print("existe o rótulo 'US'? -> ",tem_US)        
print('---------------------------')

#testa se um dado rótulo de coluna existe
tem_corVerde = 'corVerde' in paises.columns
tem_corAzul = 'corAzul' in paises.columns
print("existe o rótulo 'corVerde? -> ",tem_corVerde)        
print("existe o rótulo 'corAzul'? -> ",tem_corAzul)        
print('---------------------------')

#testa se valor faz parte de uma coluna
tem_Brasil = paises['nome'].isin(['Brasil'])
print("existe o valor 'Brasil' na coluna 'nome'?")      
print(tem_Brasil)