import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal
from datetime import datetime
# import datetime


clear_terminal()

# today = datetime.date.today()

# print('=======')
# print ('Today:', today)
# print('Year:', today.year)
# print('Month:', today.month)
# print('Day:', today.day)
# print('Weekday:', today.weekday()) # weekday returns the day of week as a number


# *************************************
# print('==== Now ====')
# # Monday  is 0, Tuesday is 1, and so on. 
# now = datetime.datetime.now()
# print('date time now: ', now)

# print ('Now:', now)  # This is the datetime object
# print ('Year now:', now.year) # prints only the year from the object
# print ('Month now:', now.month) # prints only the month from the object
# print ('Day now:', now.day) # prints only the day, as a number, from the object
# print ('Hour now:', now.hour) # prints only the hour (in UTC time)
# print ('Minute now:', now.minute) # prints only the minute
# print ('Second now:', now.second) # prints only the second


# *************************************
# print('==== A specific day in the past or future ====')
# past_date = datetime.datetime(2015, 3, 14, 9, 26)
# print (past_date)


# *************************************
# print('==== Find the duration between two dates ====')
# past_date = datetime.datetime(2010, 3, 14, 9, 26)
# print (past_date)

# current_date = datetime.datetime.now()
# delta = (current_date - past_date)
# print (delta)

# print('Duration: ', current_date.year - past_date.year)


# *************************************
# print('==== Find a date that is two weeks from an existing date in your records ====')
# start_date = datetime.date(2023, 7, 15) # known date
# end_date = start_date + datetime.timedelta(weeks=2) #unknown date

# print(start_date)
# print (end_date)

# *************************************
# print('==== Converting a string value in this format to a date object ====')
# from datetime import date
# new_date_obj = date.fromisoformat("2023-07-15")
# print (new_date_obj)


# *************************************
# print('==== strptime() function ====')
# date_string = "1/1/2000"
# date_format = "%m/%d/%Y"

# new_date = datetime.strptime(date_string, date_format)
# print (new_date)


# *************************************
# print('==== strptime() function ====')
# date_string = "12 May, 2022"
# date_format = "%d %B, %Y" # the format need to match the date_string
# new_date = datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)


# date_string = "Mar 10 2020 08:27"
# date_format = "%b %d %Y %I:%M" #FILL THIS IN
# new_date = datetime.strptime(date_string, date_format)
# print (f"{date_string} converts to", new_date)


# *************************************
print('==== Use the strftime() method %B shortcut to extract the full name of the month ====')
new_date = datetime(2020, 7, 31)
print (new_date.strftime("%B"))





                       