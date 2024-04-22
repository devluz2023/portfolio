# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:26:14 2019

@author: ecorrea
"""

#P15: Importação de CSV padrão para um DataFrame
import pandas as pd

paises = pd.read_csv("c:/bases/paises.csv",index_col="sigla")
print(paises)