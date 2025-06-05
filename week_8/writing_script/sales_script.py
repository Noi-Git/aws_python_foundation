import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal

clear_terminal()

import random
from product_sales import Product

#======= Add sale data to Product ========
product_data = [("widgetA", 5.99, 100), ("widgetB", 10.99, 100),
            ("widgetC",14.99 , 200), ("widgetD", 16.99, 50),
            ("widgetE",14.99 , 125), ("widgetF", 11.99, 75),
            ("widgetG",4.99 , 200), ("widgetH", 17.99, 200),
            ("widgetI",1.99 , 300), ("widgetJ", 13.99, 50)]

def create_product_objects(data):
    products = []
    for product in product_data:
        name, price, quant = product
        products.append(Product(name, price, quant))
    return products


#======= Sales ========
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
      # print('+++', sale['product'])
      # print('***', product)
      quantity_sold = sum(quants)
      revenue = round(product.price * quantity_sold, 2)
      report += f'{product}: {quantity_sold} sold for a total revenue of ${revenue}\n'
    report += f'Total Sales: ${total_sale}\n'
    return report
 
'''
Use random.randint function chooses a random quantity for each sale. Then, add_sale records a sale on the Sales object. Finally, the function returns a sales report. 

''' 
def report_sales(product_list):
    sales = Sales()
    for e, i in enumerate(product_list):
        if e % 2 == 0:
            rand_num = random.randint(1, 10)
            sales.add_sale(i, rand_num)
    return sales.generate_report()


if __name__ == '__main__':
    batch1 = create_product_objects(product_data)
    print (report_sales(batch1))
  
# def test_classes():
#     prod1 = Product("WidgetA", 10.99, 100)
#     prod2 = Product("WidgetB", 19.99, 50)
#     prod3 = Product("WidgetC", 7.99, 150)
#     prod4 = Product("WidgetD", 3.99, 500)
    
#     sales = Sales()
#     sales.add_sale(prod1, 15)
#     sales.add_sale(prod2, 30)
#     sales.add_sale(prod3, 45)
#     sales.add_sale(prod1, 30)
#     sales.add_sale(prod4, 100)
    
#     sales.generate_report()  # No need to `print()` it, since the method itself prints
#     print('Sales:', sales)
#     print('prod1:', prod1)


# # ✅ Optionally run the test only when the script is executed directly:
# if __name__ == "__main__":
#     test_classes()