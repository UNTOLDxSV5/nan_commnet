import re
x=[]
file_list=[]
final_path=''
def regex_date(paths,date_string):
    for i in paths :
        match= re.search(date_string,i)
        if match:
            x.append(i)
    return x

def final_path(day_list,next_date_string):
    for i in day_list :
        match = re.search(next_date_string,i)
        if match:
            x=i
    return x
    
def regex_match(day_list,file_check):
    for i in day_list:
        match=re.search(file_check,i)
        if match:
            file_list.append(i)
    return file_list

def final_path_match(day_list,pattern):
    for i in day_list:
        match=re.search(pattern,i)
        if match:
            final_path=i
    return final_path