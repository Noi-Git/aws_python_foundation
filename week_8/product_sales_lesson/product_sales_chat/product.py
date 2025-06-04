import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal

clear_terminal()

class Product:
  def __init__(self, name, price, stock):
    self.name = name
    self.price = price
    self.stock = stock

  def __str__(self):
    return f'Product name: {self.name}, Price: ${self.price}, Amount in stock: {self.stock}'

# #======= Test data ========
# prod1= Product("WidgetA", 1.26, 50)
# print(f'{prod1.name}: {prod1.price}: {prod1.stock}')
# print(f'Prod1: {prod1}') #This will call the __str__
