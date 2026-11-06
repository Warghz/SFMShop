# Файл src/models/product.py
class Product:

    def __init__(self, name, price, quantity):
        self.name = name
        if price < 0:
            raise ValueError("Цена не может быть отрицательной!")
        self.price = price
        if quantity < 0:
            raise ValueError("Количество не может быть отрицательным!")
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity


    def __str__(self):
        return f"Товар: {self.name}, Цена: {self.price} руб., Количество: {self.quantity}"


    def __repr__(self):
        return f"Product({self.name}, {self.price}, {self.quantity})"

    
    def __it__(self, other):
        if not isinstance(other, Product):
            return False

        return self.price < other.price


    def __eq__(self, other):
        if not isinstance(other, Product):
            return False

        return self.name == other.name and self.price == other.price


    def __str__(self):
        return f"Товар {self.name}, Цена: {self.price}, Количество: {self.quantity}"


    