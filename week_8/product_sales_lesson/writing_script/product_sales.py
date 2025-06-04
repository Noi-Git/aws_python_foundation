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