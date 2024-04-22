# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:09:18 2019

@author: ecorrea
"""

#P12: Propriedades básicas dos DataFrames
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

#recupera e imprime as propriedades 
print('-----------')
num_linhas = paises.shape[0]
num_colunas = paises.shape[1]
indices = paises.index                 
colunas = paises.columns
paises_tipo = type(paises)             
paises_dtypes = paises.dtypes
paises_idx_dtype = paises.index.dtype  

print('número de linhas: ', num_linhas)
print('número de colunas: ', num_colunas)
print('rótulos das linhas: ', indices)
print('rótulos das colunas: ', colunas)
print('tipo (type): ',paises_tipo)
print('dtypes das colunas:\n', paises_dtypes)
print('dtype dos rótulos das linhas:', paises_idx_dtype) 