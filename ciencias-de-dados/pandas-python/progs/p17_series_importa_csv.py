# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:33:47 2019

@author: ecorrea
"""

#P17: Importação de arquivo com série temporal
import pandas as pd

#importa o arquivo para uma Series
serie_gols = pd.read_csv("c:/bases/gols.txt", sep=" ", 
                     squeeze=True, index_col=0)

#converte o tipo do índice para datetime e imprime a série
serie_gols.index = pd.to_datetime(serie_gols.index, 
                                      format='%d/%m/%Y')
print(serie_gols)