import pandas as pd
import numpy as np
import os
from datetime import date,datetime,timedelta
import re
import calendar
import datetime
from util.list_files import list_files
from util.get_dates import get_dates
from util.matching import regex_date,final_path,regex_match
from config.config import get_directory_path

directory_reconcilation=get_directory_path("directory_reconcilation")

paths=list_files(directory_reconcilation,'.xlsx')

today,day_name,date_string=get_dates()
#date_string='2025-06-12'

day_list=regex_date(paths,date_string)

file_check='zema_cxl_exceptions_'
file_list=regex_match(day_list,file_check)

next_date=today+timedelta(days=1)
next_date_string=next_date.strftime("%Y-%m-%d")
#next_date_string='2025-06-13'

final_path=final_path(file_list,next_date_string)
df=pd.read_excel(final_path,sheet_name=['exceptions_quotes_da'])

x=df['exceptions_quotes_da']
x=x.loc[(x['comment'].isnull() & x['CURVE_NAME'].notnull())]

print(x)
      
x.to_csv(r'outputs\reconcilation.csv')
