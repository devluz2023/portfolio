# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:36:33 2019

@author: ecorrea
"""

#P31 Gráfico de linhas
import pandas as pd

dados = {"óleo de soja": [71.15, 66.93, 67.91, 67.66],
         "melancia": [10.52, 15.68, 14.95, 26.23],
         "frango congelado": [47.17, 23.68, 38.36, 17.08]
         }

df = pd.DataFrame(dados,index=[3,6,9,12])

lines = df.plot(kind="line", 
                style=[".-","+-","*-"], 
                ylim=(0,100), xlim=(3,12))