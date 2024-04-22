# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:41:14 2019

@author: ecorrea
"""

#P32 Gráfico de barras vertical
import pandas as pd

df = pd.DataFrame([70, 25, 50], 
                  index=["teatro", "escultura", "pintura"])

barras = df.plot(kind="bar", legend=False)