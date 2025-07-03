import pandas as pd
import numpy as np
import os
from datetime import date,datetime,timedelta
import re
import calendar
import datetime

final_bau_reports='DQC Report\DQC Report\BauReports\FinalBauReports'

def list_files(filepath, filetype):
   paths = []
   for root, dirs, files in os.walk(filepath):
      for file in files:
         if file.lower().endswith(filetype.lower()):
            paths.append(os.path.join(root, file))
   return(paths)

paths=list_files(final_bau_reports,'.xlsx')

                        #Dynamic
today=datetime.date.today()
day_name=calendar.day_name[today.weekday()].lower()
date_string = today.strftime("%Y-%m-%d")
print(date_string)
print('----------------')
#date='2025-06-12'

day_list=[]
for i in paths :
    match= re.search(date_string,i)
    if match:
        day_list.append(i)
print(day_list)
print('----------------')
                  # Dynamic
if day_name=='friday' :
    next_date=today+timedelta(days=3)
else :
    next_date=today+timedelta(days=1)
    
next_date_string=next_date.strftime("%Y-%m-%d")

#next_date='2025-06-13'
final_path=''
for i in day_list :
   match = re.search(next_date_string,i)
   if match:
      final_path=i
print(final_path)
print('----------------')

df=pd.read_excel(final_path,index_col=0)

x=df.loc[(df['comment'].isnull() & df['curve_list'].notnull())]

print(x)
      
x.to_csv(r'outputs\baureports.csv')
