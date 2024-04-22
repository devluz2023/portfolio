# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:25:13 2019

@author: ecorrea
"""

#P24 Estatísticas básicas: medidas de variabilidade
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
         "juiz_A": [4,1,3,2,4,4,2],
         "juiz_B": [2,1,4,1,1,5,6]
         }

df = pd.DataFrame(dados)

#calcula as medidas de variabilidade 
print("Juiz A:")
print("-------")
print("amplitude:", df['juiz_A'].max() - df['juiz_A'].min())
print("variância:", df['juiz_A'].var())
print("desvio padrão:", df['juiz_A'].std())

print("\nJuiz B")
print("-------")
print("amplitude:", df['juiz_B'].max() - df['juiz_B'].min())
print("variância:", df['juiz_B'].var())
print("desvio padrão:", df['juiz_B'].std())