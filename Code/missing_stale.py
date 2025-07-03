import pandas as pd
import numpy as np
import os
from datetime import date,datetime,timedelta
import re
import calendar
import datetime

dirc='DQC Report\DQC Report\Curve Reports\Curve Data -Missing Stale'

def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)

paths=list_files(dirc,'.xlsx')

#print(paths)
today=datetime.date.today()
date_string = today.strftime("%Y-%m-%d")
#date_string='2025-06-12'

day_list=[]
for i in paths :
   match=re.search(date_string,i)
   if match :
      day_list.append(i)
#print(day_list)

file_check='missing'
file_list=[]
for i in day_list:
   match=re.search(file_check,i)
   if match:
      file_list.append(i)
#print(file_list)

pattern=r'\d+T\d+'
final_path=''
for i in day_list:
   match=re.search(pattern,i)
   if match:
      final_path=i
print(final_path)

df=pd.read_excel(final_path,index_col=0,sheet_name=['curve_data_missing','curve_data_stale'])

df1=df['curve_data_missing']
df2=df['curve_data_stale']

x1=df1.loc[(df1['comment'].isnull() & df1['pos_unpriced_bbl_abs']>0)]
y1=df2.loc[(df2['comment'].isnull() & df2['pos_unpriced_bbl_abs']>0)]

print(x1)
print('--------')
print(y1)
      
x1.to_csv(r'outputs\curve_data_missing.csv')
y1.to_csv(r'outputs\curve_data_stale.csv')