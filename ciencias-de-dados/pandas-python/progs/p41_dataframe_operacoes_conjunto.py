# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:10:56 2019

@author: ecorrea
"""

#P41: Operações de conjunto
import pandas as pd

#(1)-Cria dois DataFrames com e-mails
df_sql = pd.DataFrame({"email":["rakesh@xyz.com",
                                "ecg@acmecorpus.com"]})

df_python = pd.DataFrame({"email":["ana@xyz.com",
                                   "jonas@acmecorpus.com",
                                   "rakesh@xyz.com"]})

#(2)-Efetua as operações de conjunto

#2.1 União (relação de alunos distintos) 
alunos = pd.concat([df_sql, df_python], ignore_index=True)
alunos = alunos.drop_duplicates()

#2.2 Interseção (quem fez ambos os cursos)
sql_e_python = df_sql.merge(df_python) 

#2.3 Diferença (quem fez só SQL e quem fez só R)
so_sql = df_sql[df_sql.email.isin(df_python.email)==False]
so_python = df_python[df_python.email.isin(df_sql.email)==False]

#(3)-Imprime os resultados
print('------------------------------')
print('Alunos Distintos:')
print(alunos)
print('------------------------------')
print('Alunos cursaram SQL e Python:')
print(sql_e_python)
print('------------------------------')
print('Alunos cursaram apenas SQL:')
print(so_sql)
print('------------------------------')
print('Alunos cursaram apenas Python:')
print(so_python)