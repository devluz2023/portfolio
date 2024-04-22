# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:32:21 2019

@author: ecorrea
"""

#P01: Hello Series!
import pandas as pd

#cria a Series notas
notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.4])

#cria a Series alunos
lst_matriculas = ['M02','M05','M13','M14','M19']
lst_nomes = ['Bob','Dayse','Bill','Cris','Jimi']
alunos = pd.Series(lst_nomes,index=lst_matriculas)

#imprime as duas Series
print(notas); print("---------------"); print(alunos)