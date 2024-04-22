# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 18:36:32 2019

@author: ecorrea
"""

#P02: Propriedades básicas das Series
import pandas as pd

#cria a Series "alunos"
alunos = pd.Series({'M02':'Bob','M05':'Dayse','M13':'Bill',
                    'M14':'Cris','M19':'Jimi'})

#atribui nomes p/ os vetores de dados e rótulos
alunos.name = "alunos"             
alunos.index.name = "matrículas"    

#recupera e imprime as propriedades 
print(alunos)
print('-----------')
tamanho = alunos.size                  
dados   = alunos.values                
rotulos = alunos.index                 
alunos_tipo = type(alunos)             
alunos_dtype = alunos.dtype            
alunos_idx_dtype = alunos.index.dtype  

print('número de elementos: ', tamanho)
print('vetor de dados: ', dados)
print('vetor de rótulos: ', rotulos)
print('tipo (type): ', alunos_tipo)
print('dtype da Series:', alunos_dtype)
print('dtype do vetor de rótulos:', alunos_idx_dtype)