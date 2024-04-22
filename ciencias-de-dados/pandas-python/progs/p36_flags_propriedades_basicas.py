# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:52:02 2019

@author: ecorrea
"""

#P36: Estudando a base de dados flags
#     I. Propriedades básicas de cada atributo
import pandas as pd

#------------------------------------------------------
#(1)-Importa a base de dados
#------------------------------------------------------
flags = pd.read_csv('c:/bases/flags.csv')

#------------------------------------------------------
#(2)-Obtém as propriedades básicas de cada atributo
#------------------------------------------------------
i=0
for c in flags.columns: 
    i +=1
    att = flags[c]                       #atributo
    att_dtype = att.dtype                #dtype        
    att_tam_dominio =  att.unique().size #tamanho do domínio       
    att_tem_nulo = any(att.isnull())     #possui valor nulo?
    if (att_tam_dominio < 8): 
        print("("+str(i)+") atributo:", c, "\t",
              "dtype:", att_dtype, "\t",
              "nulos: ", att_tem_nulo, "\n",
              "domínio:", att.unique())
    else:
        if (att_dtype=='object'): 
            print("("+str(i)+") atributo:", c, "\t",
                  "dtype:", att_dtype, "\t",
                  "nulos: ", att_tem_nulo, "\n",
                  "domínio (primeiros elementos):", att.unique()[0:8])
        else:
            print("("+str(i)+") atributo:", c, "\t",
                  "dtype:", att_dtype, "\t",
                  "nulos: ", att_tem_nulo, "\n",
                  "min: ", att.min(), "\t", 
                  "max: ", att.max(), "\t", 
                  "média: ", round(att.mean(),2), "\t", 
                  "d.p.: ", round(att.std(),2))
