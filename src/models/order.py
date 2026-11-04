from utils.calculations import calculate_total
from .product import Product

class Order():

    def __init__(self, user, products, order_id):
        self.user = user
        self.products = products
        self.order_id = order_id


    def total_price(self):
        total = 0
        for product in self.products:
            total = total + product.get_total_price()
        return total


    def __str__(self):
        return f"Заказ #{self.order_id} на сумму {self.total_price()} руб. (Пользователь: {self.user})"

    