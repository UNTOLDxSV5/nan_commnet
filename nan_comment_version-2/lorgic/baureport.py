import pandas as pd
from datetime import timedelta
from util.list_files import list_files
from util.list_files import list_files
from util.get_dates import get_dates
from util.matching import regex_date,final_path
from config.config import get_directory_path

directory_bau_reports=get_directory_path("directory_bau_reports")

paths=list_files(directory_bau_reports,'.xlsx')

today,day_name,date_string=get_dates()
#date_string='2025-07-03'

day_list=regex_date(paths,date_string)

if day_name=='friday' :
    next_date=today+timedelta(days=3)
else :
    next_date=today+timedelta(days=1)
   
next_date_string=next_date.strftime("%Y-%m-%d")
#next_date='2025-07-04'

final_path=final_path(day_list,next_date_string)

df=pd.read_excel(final_path,index_col=0)
x=df.loc[(df['comment'].isnull() & df['curve_list'].notnull())]

print(x)
      
x.to_csv(r'outputs\baureports.csv')

