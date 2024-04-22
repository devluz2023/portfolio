# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:09:05 2019

@author: ecorrea
"""

#P40: Concatenação de DataFrames Incompatíveis
import pandas as pd

#(1)-Cria dois DataFrames com definição diferente
d1 = pd.DataFrame({"carro":["Hyundai", "Renault", "Fiat"]})
d2 = pd.DataFrame({"animal":["Capivara", "Bem-te-vi"]})

#(2)-Concatena os DataFrames
d3 = pd.concat([d1,d2], ignore_index=True, sort=False)

print(d3)      