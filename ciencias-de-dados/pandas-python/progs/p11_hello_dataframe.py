# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:04:17 2019

@author: ecorrea
"""

#P11: Hello DataFrame!
import pandas as pd

#cria o DataFrame
dados = {'nome': ['Argentina','Brasil','França','Itália',
                  'Reino Unido'],
         'continente': ['América','América','Europa','Europa',
                        'Europa'],
         'extensao': [2780,8511,644,301,244],
         'corVerde': [0,1,0,1,0]
         }

siglas = ['AR','BR','FR','IT','UK']

paises = pd.DataFrame(dados,index=siglas)

#imprime o DataFrame
print(paises)