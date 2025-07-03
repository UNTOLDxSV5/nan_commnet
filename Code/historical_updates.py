import pandas as pd
import numpy as np
import os
from datetime import date,datetime,timedelta
import re
import calendar
import datetime

dirc='DQC Report\DQC Report\Curve Reports\Pricing - Historical updates'

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

pattern=r'\d+T\d+'
final_path=''
for i in day_list:
   match=re.search(pattern,i)
   if match:
      final_path=i
print(final_path)

df=pd.read_excel(final_path,index_col=0)

x=df.loc[(df['comment'].isnull() & df['pos_unpriced_bbl']>0)]

print(x)
      
x.to_csv(r'outputs\historical_updates.csv')