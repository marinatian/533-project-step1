# discounts.py

class DiscountManager:
    def __init__(self):
        self.discounts = {}

    def add_discount(self, product_id, discount_rate):
        if not 0 <= discount_rate <= 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        self.discounts[product_id] = discount_rate

    def remove_discount(self, product_id):
        if product_id not in self.discounts:
            raise KeyError(f"No discount found for product ID {product_id}.")
        del self.discounts[product_id]

    def apply_discount(self, product_id, price):
        if product_id not in self.discounts:
            return price
        return price * (1 - self.discounts[product_id])
