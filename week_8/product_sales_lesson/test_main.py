import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from clear_terminal import clear_terminal

clear_terminal()

from product_sales import Product
from sales_script import *
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