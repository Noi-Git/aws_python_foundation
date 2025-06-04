import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) # Add root folder to the path
from week_8.product_sales_lesson.produt_sales_chat.product import *
from clear_terminal import clear_terminal
clear_terminal()

class Sales:
    def __init__(self):
        self.sales_data = []

    def add_sale(self, product, quantity):
        sale = {'product': product, 'quantity': quantity}
        self.sales_data.append(sale)

    def generate_report(self):
        print("Sales Report")
        print("============")
        total = 0
        for sale in self.sales_data:
            product = sale['product']
            quantity = sale['quantity']
            revenue = product.price * quantity
            total += revenue
            print(f"{product.name}: {quantity} units - ${revenue:.2f}")
        print(f"Total Revenue: ${total:.2f}")
