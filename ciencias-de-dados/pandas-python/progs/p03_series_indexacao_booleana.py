# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:51:50 2019

@author: ecorrea
"""

#P03: Indexação booleana
import pandas as pd

#cria as Series "notas" e "alunos"
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
                    'M14':'Cris','M19':'Jimi'})

#obtém os índices dos alunos aprovados
idx_aprovados = notas[notas >= 7].index

#imprime os alunos aprovados
print('relação de alunos aprovados:')
print('---------------------------')
print(alunos[idx_aprovados])

