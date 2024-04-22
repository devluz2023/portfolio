# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 18:28:49 2019

@author: ecorrea
"""

#P29 Agregação com o método `group_by()`
import pandas as pd  

#1-cria o DataFrame
dados = {"sexo": ["F","M","F","F","F","M"],
         "bairro": ["Belverde",
                    "Belverde",
                    "Savassi",
                    "Anchieta",
                    None,
                    "Savassi"],
         "valor": [150.00,
                    35.00,
                    80.00,
                    250.00,
                    9.90,
                    25.00],                   
         "cartao": ["Master",
                    "Visa",
                    "Visa",
                    "Amex",
                    "Elo",
                    "Master"]}

id_clientes = [1,2,3,4,5,6]

vendas = pd.DataFrame(dados, index=id_clientes)

#2-Gera uma variável "grouped" 
#  onde a chave é "bairro" e a medida "valor"
grupo_valor_bairro = vendas['valor'].groupby(vendas['bairro'])

#3-Computa agregados a partir da variável gerada
print('- quantidade de clientes, por bairro:\n ',grupo_valor_bairro.count())
print('--------------------------------------')
print('- valor total das vendas, por bairro:\n ',grupo_valor_bairro.sum())
print('--------------------------------------')
print('- valor médio das vendas, por bairro:\n ',grupo_valor_bairro.mean())

grupo_valor_sexo_bairro = vendas['valor'].groupby([vendas['sexo'], vendas['bairro']])
print('- valor total das vendas, por bairro:\n ',grupo_valor_sexo_bairro.sum())
