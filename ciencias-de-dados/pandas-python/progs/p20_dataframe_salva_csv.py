# -*- coding: utf-8 -*-
"""
Created on Tue Oct  1 17:41:40 2019

@author: ecorrea
"""

#P20: Salva o conteúdo de um DataFrame em um CSV.
import pandas as pd

#cria o DataFrame
dados = {'codigo': [1001,1002,1003,1004,1005],
         'nome': ['Leite','Café','Biscoito','Chá',
                  'Torradas']
         }

produtos = pd.DataFrame(dados)

#salva o seu conteúdo para um arquivo
produtos.to_csv("C:/bases/produtos.csv", sep="\t", index=False)