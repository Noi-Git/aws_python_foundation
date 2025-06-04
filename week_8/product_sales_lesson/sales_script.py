import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal
clear_terminal()

# from product_sales import Product
# from test_main import test_classes

class Sales:
  def __init__(self):
    self.sales_data = []

  def add_sale(self, product, quantity):
    sale = {'product': product, 'quantity': quantity}
    self.sales_data.append(sale)
    print('self.sales_data:', self.sales_data)

  def generate_report(self):
    total_sale = 0
    print('This is sales data: ', self.sales_data) #This will show data in each sale, such as sale001

    for sale in self.sales_data:
      print('each sale:', sale)
      total_sale += sale['product'].price * sale['quantity']

    report = ''
    product_set = set([sale['product'] for sale in self.sales_data])

    for product in product_set:
      quants = [sale['quantity'] for sale in self.sales_data if sale['product'] == product]
      quantity_sold = sum(quants)
      revenue = round(product.price * quantity_sold, 2)
      report += f'{product}: {quantity_sold} sold for a total revenue fo ${revenue}\n'
    report += f'Total Sales: ${total_sale}\n'
    return report

# test_classes()

# prod1 = Product("WidgetA", 10.99, 100)
# prod2 = Product("WidgetB", 19.99, 50)
# prod3 = Product("WidgetC", 7.99, 150)
# prod4 = Product("WidgetD", 3.99, 500)

# sales = Sales()
# sales.add_sale(prod1, 15)
# sales.add_sale(prod2, 30)
# sales.add_sale(prod3, 45)
# sales.add_sale(prod1, 30)
# sales.add_sale(prod4, 100)


#======= Test data ========
# sale001 = Sales() #First need to create an object call sale001
# sale001.add_sale("tea cup", 5) #call method add-sale
# sale001.add_sale("tea bag", 2)
# sale001.add_sale("kattle", 1)
# sale001.add_sale("milk", 1)

# sale002 = Sales() #First need to create an object call sale001
# sale002.add_sale("coffe cup", 12) #call method add-sale
# sale002.add_sale("coffee beans", 4) #call method add-sale
# sale002.add_sale("milk", 1) #call method add-sale

# sale003 = Sales() #First need to create an object call sale001
# sale003.add_sale("coffee mug", 1) #call method add-sale

# print(f'Sale data: {sale001.sales_data}') # It is calling line:10 self.sale_data = [value added on line:18]. self mean sale001
# print(f'Sale data: {sale002.sales_data}') # It is calling line:10 self.sale_data = [value added on line:18]. self mean sale002
# print(f'Sale data: {sale003.sales_data}') # It is calling line:10 self.sale_data = [value added on line:18]. self mean sale003

# ======= To see the value inside of the sales_report =======
# print('\n======= Need to call each item in the list in order o see the value inside of the sales_report =======')
# sale.generate_report()



