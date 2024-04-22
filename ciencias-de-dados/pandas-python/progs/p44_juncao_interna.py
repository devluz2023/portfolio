# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 20:19:09 2019

@author: ecorrea
"""

#P44: Junção Interna 
import pandas as pd

#(1)-Cria os DataFrames depto e emp
dic_depto = {"id":["D1","D2","D3","D4"], 
             "nomDepto": ["Compras","RH","TI","Vendas"],
             "local":["SP","RJ","RJ","SP"]
             }

dic_emp = {"num":[3199,3269,3555,3788,3844],
           "nome": ["Ana","David","José","Marina","Luís"],
           "salario":[1600,2975,1500,5000,3000],
           "idDepto": ["D2","D3",None,"D2","D4"]
           }


depto = pd.DataFrame(dic_depto)
emp = pd.DataFrame(dic_emp) 


#(2)-Efetua a operação de junção
juncao_interna = pd.merge(emp, depto, left_on="idDepto", right_on="id")

print('------------------------------')
print("depto:")
print(depto)
print('------------------------------')
print("emp:")
print(emp)
print('------------------------------')
print("junção interna:")
print(juncao_interna)

'''
fatia = juncao_interna[['num','nome','nomDepto']]
print(fatia)

j_esq = pd.merge(emp, depto, how="left", left_on="idDepto", right_on="id")
print(j_esq)

j_dir = pd.merge(depto, emp, how="right", left_on="id", right_on="idDepto")
print(j_dir)

j_full = pd.merge(emp, depto, how="outer", left_on="idDepto", right_on="id")
print(j_full)
'''


