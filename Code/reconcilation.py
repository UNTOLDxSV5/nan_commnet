import pandas as pd
import numpy as np
import os
from datetime import date,datetime,timedelta
import re
import calendar
import datetime

dirc='DQC Report\DQC Report\Curve Reports\Reconciliation - CXL'

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
day_name=calendar.day_name[today.weekday()].lower()
date_string = today.strftime("%Y-%m-%d")
#date_string='2025-06-12'

day_list=[]
for i in paths :
   match=re.search(date_string,i)
   if match :
      day_list.append(i)
#print(day_list)

file_check='exceptions'
file_list=[]
for i in day_list:
   match=re.search(file_check,i)
   if match:
      file_list.append(i)
#print(file_list)

next_date=today+timedelta(days=1)
next_date_string=next_date.strftime("%Y-%m-%d")

#next_date_string='2025-06-13'
final_path=''
for i in file_list :
   match = re.search(next_date_string,i)
   if match:
      final_path=i
print(final_path)


df=pd.read_excel(final_path,sheet_name=['exceptions_quotes_da'])

x=df['exceptions_quotes_da']
x=x.loc[(x['comment'].isnull() & x['CURVE_NAME'].notnull())]

print(x)
      
x.to_csv(r'outputs\reconcilation.csv')
