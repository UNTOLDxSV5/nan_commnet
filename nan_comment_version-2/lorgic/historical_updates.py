import pandas as pd
import numpy as np
import os
from datetime import date,datetime,timedelta
import re
import calendar
import datetime
from util.list_files import list_files
from util.get_dates import get_dates
from util.matching import regex_date,final_path_match
from config.config import get_directory_path


directory_historical_updates=get_directory_path("directory_historical_updates")
paths=list_files(directory_historical_updates,'.xlsx')

today,day_name,date_string=get_dates()
#date_string='2025-06-12'

day_list=regex_date(paths,date_string)

pattern=r'\d+T\d+'
final_path=final_path_match(day_list,pattern)


df=pd.read_excel(final_path,index_col=0)

x=df.loc[(df['comment'].isnull() & df['pos_unpriced_bbl']>0)]

print(x)
      
x.to_csv(r'outputs\historical_updates.csv')