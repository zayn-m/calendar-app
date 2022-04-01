from .interface import ICalculateView
from datetime import date, datetime, timedelta
import time

class Calculate(ICalculateView):

    def display_age(self, date_of_birth):
        if date_of_birth == None or date_of_birth  == '':
            return {
                "error": 'Please enter a valid date'
            }

        current_date = time.time()
        date_of_birth_timestamp = time.mktime(datetime.strptime(date_of_birth, "%Y-%m-%d").timetuple())

        if date_of_birth_timestamp >= current_date:
            return {
                "error": 'Date of birth can not be greater than current date'
            }

        born_date = date_of_birth
        born = datetime.strptime(born_date, '%Y-%m-%d')
        today = date.today()
        curr_month = today.month
        born_month = born.month
        curr_day   = today.day
        born_day   = born.day
        if born_month > curr_month:
            month_diff = born_month - curr_month
        else :
            month_diff = curr_month - born_month
        if born_day > curr_day:
            day_diff = born_day - curr_day
        else :
            day_diff = curr_day - born_day 
        age = today.year - born.year
        return { "result": str(age) +"  Years   " + str(month_diff) +  "  Months  and " + str(day_diff) + "  Days" }

    def display_date_from_days(self, days):

        if days == '' or days == None:
            return { "error": 'Days can not be empty' }

        days = int(days)
        
        if days < 0:
            return { "error": 'Days can not be negative' }

        end_date = date.today() + timedelta(days=days)

        return { "result": end_date }