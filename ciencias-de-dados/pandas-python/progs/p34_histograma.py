# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:43:03 2019

@author: ecorrea
"""

#P34: Histograma
import pandas as pd

df = pd.DataFrame({
     "tempo": [4, 5, 1, 7, 7, 8, 6, 6, 5,
               2, 5, 8, 7, 1, 6, 3, 4, 8,
               5, 7, 4, 6, 3, 6, 2, 6, 8]
     })

hist = df.plot(kind="hist", bins=3)