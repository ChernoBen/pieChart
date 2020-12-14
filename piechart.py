# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:11:33 2020

@author: Benjamim
"""

import json
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

api_url_base = 'https://ccomp-pte.herokuapp.com/'

headers = {'Content-Type': 'application/json'}


def get_account_info():
  api_url = '{0}contas'.format(api_url_base)
  response = requests.get(api_url,headers=headers)
  if response.status_code == 200:
    return json.loads(response.content.decode('utf-8'))
  else:
    return None
  
var = get_account_info()
df = pd.DataFrame(var)
rotulos = df['cliente'].values
valores = df['valor'].values

fig1,ax1 = plt.subplots()
ax1.pie(valores,labels=rotulos,autopct='%1.1f%%',shadow=True, startangle=90)
ax1.axis('equal')
plt.show()
plt.savefig('contas', format='png')

