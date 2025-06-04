import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal
clear_terminal()
from product_sales import Product

class Sales:
  def __init__(self):
    self.sales_data = []

  def add_sale(self, product, quantity):
    sale = {'product': product, 'quantity': quantity}
    self.sales_data.append(sale)
    # print('self.sales_data:', self.sales_data)

  def generate_report(self):
    total_sale = 0
    print('This is sales data: ', self.sales_data) #This will show data in each sale, such as sale001

    for sale in self.sales_data:
      # print('each sale:', sale)
      print('---sale[product]:', sale['product']) #This will print data in the Product __str__
      total_sale += sale['product'].price * sale['quantity']
      # print('Total sales:', total_sale)

    report = ''
    product_set = set([sale['product'] for sale in self.sales_data])

    for product in product_set:
      quants = [sale['quantity'] for sale in self.sales_data if sale['product'] == product]
      print('+++', sale['product'])
      print('***', product)
      quantity_sold = sum(quants)
      revenue = round(product.price * quantity_sold, 2)
      report += f'{product}: {quantity_sold} sold for a total revenue of ${revenue}\n'
    report += f'Total Sales: ${total_sale}\n'
    return report
  
def test_classes():
    prod1 = Product("WidgetA", 10.99, 100)
    prod2 = Product("WidgetB", 19.99, 50)
    prod3 = Product("WidgetC", 7.99, 150)
    prod4 = Product("WidgetD", 3.99, 500)
    
    sales = Sales()
    sales.add_sale(prod1, 15)
    sales.add_sale(prod2, 30)
    sales.add_sale(prod3, 45)
    sales.add_sale(prod1, 30)
    sales.add_sale(prod4, 100)
    
    sales.generate_report()  # No need to `print()` it, since the method itself prints
    print('Sales:', sales)
    print('prod1:', prod1)
    # print (sales.generate_report())
    # print(f'Sale data: {sales.sales_data}') 

# ✅ Optionally run the test only when the script is executed directly:
if __name__ == "__main__":
    test_classes()