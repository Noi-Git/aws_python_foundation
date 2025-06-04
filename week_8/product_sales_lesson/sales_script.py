import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal

clear_terminal()

class Sales:
  def __init__(self):
    self.sales_data = []

  def add_sale(self, product, quantity):
    sale = {'product': product, 'quantity': quantity}
    self.sales_data.append(sale)

#======= Test data ========
sale001 = Sales() #First need to create an object call sale001
sale001.add_sale("tea cup", 5) #call method add-sale
print(f'Sale data: {sale001.sales_data}') # It is calling line:10 self.sale_data = [value added on line:18]. self mean sale001
