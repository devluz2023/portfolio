# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 18:06:28 2019

@author: ecorrea
"""

#p54: Criação e utilização de Função
def classe_area(area):
    if (area < 10) : 
        return 'F'
    elif (area >= 10 and area < 50) :
        return 'E'
    elif (area >= 50 and area < 100) :
        return 'D'
    elif (area >= 100 and area < 500) :
        return 'C'
    elif (area >= 500 and area < 1000) :
        return 'B'
    else :
        return 'A'
    
print('Classe de extensão territorial: ')    
print('Brasil     :', classe_area(8515))
print('Moçambique :', classe_area(801))
print('Portugal   :', classe_area(92))
print('Timor Leste:', classe_area(14))