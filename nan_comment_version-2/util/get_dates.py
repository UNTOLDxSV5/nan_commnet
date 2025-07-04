import calendar
from datetime import date,datetime,timedelta
import datetime

def get_dates():
    today=datetime.date.today()
    day_name=calendar.day_name[today.weekday()].lower()
    date_string = today.strftime("%Y-%m-%d")

    return today,day_name,date_string