# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 17:54:21 2019

@author: ecorrea
"""

#P28 Métodos unique() e value_counts()
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

#2-retorna o domínio dos atributos categóricos
print('Domínio dos atributos categóricos:')
print('---------------------------------')
print('sexo:', vendas['sexo'].unique())
print('bairro:', vendas['bairro'].unique())
print('cartao:', vendas['cartao'].unique())

#3-retorna as frequências dos valores de cada coluna
print("\n")
print('Tabelas de frequência:')
print('---------------------------------------')
print("\n1-sexo:")
print(vendas['sexo'].value_counts())
print("\n2-bairro:")
print(vendas['bairro'].value_counts())
print("\n3-cartão:")
print(vendas['cartao'].value_counts())