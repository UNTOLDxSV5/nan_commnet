import pandas as pd
from util.list_files import list_files
from util.get_dates import get_dates
from util.matching import regex_date,final_path,regex_match,final_path_match
from config.config import get_directory_path

directory_missing_stale=get_directory_path("directory_missing_stale")

paths=list_files(directory_missing_stale,'.xlsx')

today,day_name,date_string=get_dates()
# date_string='2025-07-03'

day_list=regex_date(paths,date_string)

file_check='missing_stale_curve_data_'
file_list=regex_match(day_list,file_check)

pattern=r'\d+T\d+'
final_path=final_path_match(file_list,pattern)

df=pd.read_excel(final_path,index_col=0,sheet_name=['curve_data_missing','curve_data_stale'])

df1=df['curve_data_missing']
df2=df['curve_data_stale']

x1=df1.loc[(df1['comment'].isnull() & df1['pos_unpriced_bbl_abs']>0)]
y1=df2.loc[(df2['comment'].isnull() & df2['pos_unpriced_bbl_abs']>0)]

print(x1)
print(y1)

x1.to_csv(r'outputs\curve_data_missing.csv')
y1.to_csv(r'outputs\curve_data_stale.csv')