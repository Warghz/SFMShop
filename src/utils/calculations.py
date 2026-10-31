# Файл src/utils/calculations.py


def calculate_discount(price, discount_rate):
    return price * discount_rate


def calculate_total(price, quantity):
    return price * quantity


def calculate_order_total(discount_rate: float, price: int, ) -> float:
    result = price * (1 - discount_rate)
    return round(result, 2)


def get_discount_by_total(total):
    if total <= 0:
        return 0
     
    if total > 10000:
        discount = 0.15 
    elif total > 5000:
        discount = 0.10
    else:
        discount = 0.05

    return discount 