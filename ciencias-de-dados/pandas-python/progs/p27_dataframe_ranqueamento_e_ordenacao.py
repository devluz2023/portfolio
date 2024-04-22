# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:49:49 2019

@author: ecorrea
"""

#P27 Métodos sort_values() e rank()
import pandas as pd  

#1-cria o DataFrame da prova de 50m
dados = {"nadador": ["Simonas Bilis",
                     "Benjamin Proud",
                     "Anthony Ervin",
                     "Florent Manaudou",
                     "Andriy Hovorov",
                     "Nathan Adrian",
                     "Bruno Fratus",
                     "Brad Tandy"],
         "nacionalidade": ["Lituânia",
                           "Grã-Bretanha",
                           "Estados Unidos",
                           "França",
                           "Ucrânia",
                           "Estados Unidos",
                           "Brasil",
                           "África do Sul"],
         "tempo": [22.08,
                   21.68,
                   21.40,
                   21.41,
                   21.74,
                   21.49,
                   21.79,
                   21.79]
         }

raias = list(range(1,9))

prova50m = pd.DataFrame(dados, index=raias)
prova50m.index.name = 'raia'

#2-ordena pelo tempo de forma crescente
prova50m = prova50m.sort_values(by="tempo")
print("* * resultado final ordenado por tempo:")
print(prova50m)

#3 - gera os rankings
resultado_por_raia = prova50m['tempo'].rank(method="min")
print("\n* * posição de cada nadador (por raia):")
print(resultado_por_raia)