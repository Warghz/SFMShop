from .product import Product


class Order:

    def __init__(self, user, products, order_id, available_products):
        self.user = user
        self.products = products
        self.order_id = order_id
        self.available_products = available_products

    def add_product(self, product):
        if product not in self.available_products:
            raise KeyError("Товар не найден")

        self.products.append(product)

    def total_price(self):
        total = 0

        for product in self.products:
            total += product.get_total_price()

        return total

    def __str__(self):
        return (
            f"Заказ #{self.order_id} на сумму "
            f"{self.total_price()} руб. (Пользователь: {self.user})"
        )