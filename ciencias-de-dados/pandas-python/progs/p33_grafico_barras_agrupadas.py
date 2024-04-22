# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:42:21 2019

@author: ecorrea
"""

#P33: gráfico de barras agrupadas
import pandas as pd

df = pd.DataFrame({"mulheres": [40,10,30], 
                   "homens": [30,15,20]},
                  index=["teatro", "escultura", "pintura"])

barras = df.plot(kind="bar", legend=True, color=["yellow", "blue"])