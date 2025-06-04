import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from clear_terminal import clear_terminal
from datetime import datetime, timedelta

clear_terminal()

'''
Write a function that takes a date as input and returns the number of days until the next Friday.
'''

def day_until(date):
  date_string = date
  date_format = "%m-%d-%Y"
  new_date = datetime.strptime(date_string, date_format)

  # covert the format
  formated_date = new_date.strftime("%m/%d/%Y")
  week_day = new_date.strftime("%A")
  week_day_int = int(new_date.strftime("%w"))
  print('Week day: ', week_day)

  # Friday is = 5
  days_until_friday = (5 - week_day_int) % 7
  # days_until_friday = 7 if days_until_friday == 0 else days_until_friday
  # print(f'Today is {week_day}. It is {days_until_friday} until Friday')
  if days_until_friday == 0:
    print("Today is Friday", days_until_friday)
  else:
    print("You have to wait", days_until_friday, "more days until Friday.")
  return formated_date

print('Day until: ', day_until("07-28-2023"))
print('Day until: ', day_until("07-29-2023"))
print('Day until: ', day_until("08-02-2023"))
