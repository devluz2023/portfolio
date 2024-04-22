# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:26:48 2019

@author: ecorrea
"""

#P25 Boxplot - comparação de distribuições
import pandas as pd  

df = pd.DataFrame({
        "homens":[4, 2, 7, 3, 1, 4, 2, 4, 8, 1],
        "mulheres": [5, 4, 6, 5, 4, 2, 6, 6, 4, 3]
        })

boxplot = df.boxplot(column=['homens','mulheres'], 
                     showmeans=True)