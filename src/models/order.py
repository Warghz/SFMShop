from utils.calculations import calculate_total
from .product import Product

class Order():

    def __init__(self, user, products):
        self.user = user
        self.products = products


    def total_price(self):
        total = 0
        for product in self.products:
            total = total + product.get_total_price()
        return total