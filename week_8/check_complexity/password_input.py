import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal
clear_terminal()

from password_check import check_password_strength

strong_password = False
  
while strong_password == False:
  user_password = input("Please create a password: ")

  score = check_password_strength(user_password)

  if score < 4:
    print(f'Password has {score} charecters. It is not strong enough!')
  elif score in (4,5):
    strong_password = True
    print(f'Password has {score} charecters. It is moderate!')
  else:
    strong_password = True
    print(f'Password has {score} charecters. It is strong!')
