import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal
clear_terminal()

'''
1. Create the module file. Define functions to check if the user included special characters, uppercase letters, lowercase letters, and numbers. Each check should add a point to the overall strength score if the check is successful.

2 Return a strength score for each password that it checks.

3 Write a script that imports the appropriate function(s), and asks the user to input a password. When the program runs, it should print out the strength of the provided password and a message about whether it is strong enough, or if the user should try again.
'''

# class Check:
#   def __init__(self, text):
#     self.text = text

def check_password_strength(text):
  # if uppercase add 1 to the count
  count_strangth = 0
  special_char = '!"#$%&\'()*+,-./:;<=>?@[\]^`{|}~'
  number = '0123456789'
  
  if any(char.isupper() for char in text):
    count_strangth += 1

  if any(char.islower() for char in text):
    count_strangth += 1

  for special in special_char:
    if special in text:
      count_strangth += 1

  if any(num in number for num in text):
      count_strangth += 1
  
  if len(text) >= 8:
    count_strangth += len(text) - 4

  
  return count_strangth

# password = Check()
# my_password = check_password_strength('No@1n6')
# print('count:', my_password)

