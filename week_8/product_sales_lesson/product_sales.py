import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal

clear_terminal()

# from test_main import * #-- This line create a circular import -- not good

class Product:
  def __init__(self, name, price, inventory):
    self.name = name
    self.price = price
    self.inventory = inventory

  def __str__(self):
    return f'Product name: {self.name}, Price: ${self.price}, Amount in stock: {self.inventory}'
  


# prod1 = Product("WidgetA", 10.99, 100)
# prod2 = Product("WidgetB", 19.99, 50)
# prod3 = Product("WidgetC", 7.99, 150)
# prod4 = Product("WidgetD", 3.99, 500)


# #======= Test data ========
# prod1= Product("WidgetA", 1.26, 50)
# print(f'{prod1.name}: {prod1.price}: {prod1.inventory}')
# print(f'Prod1: {prod1}') #This will call the __str__
