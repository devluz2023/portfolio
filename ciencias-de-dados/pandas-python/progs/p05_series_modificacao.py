# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:56:46 2019

@author: ecorrea
"""

#P05: Inserindo, Alterando e Removendo elementos de Series
import pandas as pd

#cria a Series "alunos"
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
                    'M14':'Cris','M19':'Jimi'})

print('Series original:')
print(alunos)

#insere o aluno de matrícula M55, Rakesh
alunos['M55'] = 'Rakesh'

#altera os nomes Bill, Cris e Jimi para Billy, Cristy e Jimmy
alunos['M13'] = 'Billy'
alunos[['M14','M19']] = ['Cristy','Jimmy']

#remove o aluno de matrícula M02 (Bob)
alunos = alunos.drop('M02')

print('---------------------------')
print('Series após as alterações:')
print(alunos)