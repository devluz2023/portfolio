# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:16:56 2019

@author: ecorrea
"""

#P43: Junção Natural
import pandas as pd

#(1)-Cria os DataFrames R e S
R = pd.DataFrame({"a":[1,7], 
                  "b":[2,4]})

S = pd.DataFrame({"b":[2,4,9], 
                  "c":[3,6,1],
                  "d":[5,9,5]})


#(2)-Efetua a operação de junção
juncao_natural = pd.merge(R, S)

print('------------------------------')
print("R:")
print(R)
print('------------------------------')
print("S:")
print(S)
print('------------------------------')
print("junção natural entre R e S:")
print(juncao_natural)