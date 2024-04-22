# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:06:58 2019

@author: ecorrea
"""

#P39: Concatenação de DataFrames
import pandas as pd

#(1)-Cria os DataFrames com as vendas de cada loja
lojaA = pd.DataFrame({"loja":["A", "A", "A"],
                      "dia": ["sex", "sab", "dom"],
                      "valor": [7500, 9500, 8200]}
                      )

lojaB = pd.DataFrame({"loja":["B", "B", "B"],
                      "dia": ["sex", "sab", "dom"],
                      "valor": [5100, 8250, 9900]}
                      )

lojaC = pd.DataFrame({"loja":["C", "C"],
                      "dia": ["sab", "dom"],
                      "valor": [7500, 11800]}
                      )

#(2)-Concatena tudo em um único DataFrame
lojasABC = pd.concat([lojaA,lojaB,lojaC], ignore_index=True)

print(lojasABC)                   