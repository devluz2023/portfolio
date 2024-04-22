# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:47:26 2019

@author: ecorrea
"""

#P26 Estatísticas sobre colunas e linhas de um DataFrame
import pandas as pd  

#cria uma DataFrame com as notas de 4 alunos em 3 provas
notas = pd.DataFrame({"A1":[9.8, 7.2, 8.0],
                      "A2": [5.3, 4.0, 3.5],
                      "A3": [5.5, 8.1, 7.2],
                      "A4": [7.0, 7.5, 6.5]}, 
                      index=["P1","P2","P3"])

#imprime o DataFrame
print("\nnotas finais: ")
print('-----------------------------')
print(notas)

#computa e imprime as estatísticas por aluno e prova
print('\nmédia de cada aluno:')
print('-----------------------------')
print(notas.mean())

print('\nmaior nota de cada aluno:')
print('-----------------------------')
print(notas.max())

print('\nmédia de cada prova:')
print('-----------------------------')
print(notas.mean(axis=1))

print('\nmaior nota de cada prova:')
print('-----------------------------')
print(notas.max(axis=1))