# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:36:11 2019

@author: ecorrea
"""

#P18: Importação de planilha Excel
import pandas as pd

cidades = pd.read_excel("c:/bases/capitais.xlsx")
print(cidades)