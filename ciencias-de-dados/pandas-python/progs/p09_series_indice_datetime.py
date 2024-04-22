# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:11:10 2019

@author: ecorrea
"""

#P09: Índices datetime
import pandas as pd  

#(1)-cria a série temporal
dias = ['10/02/2019', '11/02/2019','12/02/2019','13/02/2019',
        '14/02/2019','15/02/2019']
temp_max = [31,35,34,28,27,27]

serie_temporal = pd.Series(temp_max,index=dias)

#(2)-converte o tipo do índice para datetime e imprime a série
serie_temporal.index = pd.to_datetime(serie_temporal.index, 
                                      format='%d/%m/%Y')
print(serie_temporal)