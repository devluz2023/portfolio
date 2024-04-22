# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 19:05:36 2019

@author: ecorrea
"""

#P07: Operações aritméticas com computação vetorizada
import pandas as pd
import numpy as  np

#cria as Series s1 e s2
s1 = pd.Series([2,4,6])
s2 = pd.Series([1,3,5])
print('s1:'); print(s1)
print('s2:'); print(s2)

#efetua as operações aritméticas
print('---------------------------')
print('s1 * 2')
print(s1 * 2)          
print('---------------------------')
print('s1 + s2')
print(s1 + s2)
print('---------------------------')
print('raiz quadrada dos elementos de s1')
print(np.sqrt(s1))   #com a Numpy!