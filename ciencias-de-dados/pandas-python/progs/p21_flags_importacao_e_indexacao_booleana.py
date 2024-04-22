# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:47:02 2019

@author: ecorrea
"""

#P21: Quais os países que também tem verde, amarelo, azul
#     e branco entre as cores de sua bandeira nacional?
import pandas as pd

#------------------------------------------------------
#(1)-Importa a base de dados
#------------------------------------------------------
flags = pd.read_csv('c:/bases/flags.csv')

#------------------------------------------------------
#(2)-alguns métodos para obter informações básicas
#------------------------------------------------------
#imprime as primeiras linhas
print('head():'); print(flags.head())
print('-----------------------------------------------')

#imprime as últimas linhas
print('tail():'); print(flags.tail())
print('-----------------------------------------------')

#------------------------------------------------------
#(3)-quem tem verde, amarelo, azul e branco na bandeira
#------------------------------------------------------
#separa as cores
verde = flags['green']
amarelo = flags['gold']
azul = flags['blue']
branco = flags['white']
soma = verde + amarelo + azul + branco

#gera vetor booleano com True para quem tem as 4 cores
tem_todas = (soma==4)

#imprime os nomes dos países com as quatro cores
print('países com verde, amarelo, azul e branco:')
print(flags[tem_todas.values]['name'])