# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:56:00 2019

@author: ecorrea
"""

#P04: Busca em Series
import pandas as pd

#cria a Series "alunos"
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
                    'M14':'Cris','M19':'Jimi'})

#testa se rótulos fazem parte de uma séries
tem_M13 = 'M13' in alunos
tem_M99 = 'M99' in alunos
print("existe o rótulo 'M13'? -> ",tem_M13)        
print("existe o rótulo 'M99'? -> ",tem_M99)        
print('---------------------------')

#testa se valor faz parte de uma séries
tem_Bob = alunos.isin(['Bob'])
print("existe o valor 'Bob'")      
print(tem_Bob)