# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:10:03 2019

@author: ecorrea
"""

#P22 Tipos de atributos
import pandas as pd  

#cria o DataFrame "pme"
dados = {"renda": [6.46, 1.50, 0.00, 
                   2.57, 9.90, 6.22],
         "empregos": [1,1,0,1,2,3],
         "sexo": ["F","M","F","M","M","F"],
         "escolaridade": ["pós-graduação","fundamental",
                          "médio","médio",
                          "superior","médio"]
         }

pme = pd.DataFrame(dados)

#imprime o nome de cada atributo e seu dtype
print("\natributos e seus dtypes:")
print("------------------------")
print(pme.dtypes)