from datetime import datetime

def next_friday(date_string):
  date_formant = "%m/%d/%Y"
  date = datetime.strptime(date_string, date_formant) #Convert the date to a datetime object.
  weekday = date.weekday() #Get the weekday associated with the date.

  # Calculate the number of days until the next weekday
  if weekday <= 4:
    num_days = 4 - weekday #Friday has a weekday value of 4
  else:
    num_days = 11 - weekday #Counts into a new week, 7+4
  return num_days

print(next_friday("07/28/2023"))
print(next_friday("07/29/2023"))
print(next_friday("08/02/2023"))