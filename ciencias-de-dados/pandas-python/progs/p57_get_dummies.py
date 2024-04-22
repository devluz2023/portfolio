# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:15:46 2019

@author: ecorrea
"""

#P57: Normalização de atributo categórico
import pandas as pd

#1-Importa as bases de dados
flags = pd.read_csv('c:/bases/flags.csv')

#2-realiza a transformação com get_dummies() e join()
dummies = pd.get_dummies(flags['language'], prefix='lg')
flags = flags.join(dummies)

print(flags[["language",
             "lg_1",
             "lg_2",
             "lg_3",
             "lg_4",
             "lg_5",
             "lg_6",
             "lg_7",
             "lg_8",
             "lg_9",
             "lg_10"
        ]])