# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:14:46 2019

@author: ecorrea
"""

#P23 Estatísticas básicas: medidas de tendência central
import pandas as pd  

#cria o DataFrame 
dados = {"jogador": ["Marcelo", 
                     "Pedro",
                     "Marcelo", 
                     "Adriano",
                     "Mauro", 
                     "Pedro",
                     "Marcelo"],
         "infracao": ["FALTA VIOLENTA", 
                      "RECLAMACAO",
                      "FALTA COMUM",
                      "RECLAMACAO",
                      "FALTA COMUM",
                      "FALTA VIOLENTA",
                      "RECLAMACAO"],
         "punicao": [4,1,3,2,4,4,2]
         }

df = pd.DataFrame(dados)

#calcula as medidas de tendência central
print("média:", df['punicao'].mean())
print("mediana:", df['punicao'].median())
print("moda: ", df['punicao'].mode().values)