# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:24:27 2019

@author: ecorrea
"""

#P14: Modificação de DataFrame
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

#insere o país Japão (JP)
paises.loc['JP']= {'nome': 'Japão', 
      'continente': 'Ásia', 
      'extensao': 372,
      'corVerde': 0}

#altera a extensão do Brasil
paises.at['BR','extensao']=8512

#remove a Argentina e o Reino Unido
paises = paises.drop(['AR','UK'])

print('DataFrame após as alterações:')
print(paises)