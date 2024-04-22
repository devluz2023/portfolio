# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:38:13 2019

@author: ecorrea
"""

#P19: Importação de arquivo JSON
import pandas as pd
import json

#(1)-Importa o arquivo JSON para memória
with open("c:/bases/notas.json") as f:
    j_notas = json.load(f)

#(2)-Transfere as informações para um DataFrame
notas = pd.DataFrame(j_notas, 
                     columns=['matricula','notas'])

print(notas)