# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import os
import glob

path='C:/HISMINSA/ArchivosPlanosMaestros'

all_file=glob.glob("C:/HISMINSA/ArchivosPlanosMaestros/NOMINAL*.csv")

file_list=[]

for f in all_file:
    data=pd.read_csv(f)

    file_list.append(data)
    
df=pd.concat(file_list,ignore_index=True)

df.to_csv('union_py.csv')