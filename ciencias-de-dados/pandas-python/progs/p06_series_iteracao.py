# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:58:34 2019

@author: ecorrea
"""

#P06: Iteração
import pandas as pd
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
                    'M14':'Cris','M19':'Jimi'})

#itera sobre os dados (nomes dos alunos)
for aluno in alunos: print(aluno)

#itera sobre os índices (matrículas)
for indice in alunos.index: print(indice)