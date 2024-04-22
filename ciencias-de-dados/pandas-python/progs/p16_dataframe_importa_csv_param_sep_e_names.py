# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:32:05 2019

@author: ecorrea
"""

#P16: Importação de CSV sem cabeçalho e com ";" como separador
import pandas as pd

notas = pd.read_csv("c:/bases/notas.csv", sep=";", 
                     names=['matricula','nota1','nota2'])
print(notas)