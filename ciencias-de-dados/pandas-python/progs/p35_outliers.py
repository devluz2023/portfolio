# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:48:45 2019

@author: ecorrea
"""

#P35: IQR + Boxplot
import pandas as pd

df = pd.DataFrame({
     "tempo": [4, 5, 1, 7, 7, 8, 6, 6, 5,
               2, 5, 8, 7, 1, 6, 3, 4, 8,
               5, 7, 4, 6, 3, 6, 2, 6, 18]
     })

boxplot = df.boxplot(column=['tempo'], 
                     showmeans=True)
