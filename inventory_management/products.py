# products.py

class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, name, price):
        if product_id in self.products:
            raise ValueError("Product ID already exists.")
        self.products[product_id] = {"name": name, "price": price}

    def remove_product(self, product_id):
        if product_id not in self.products:
            raise KeyError("Product not found.")
        del self.products[product_id]

    def update_product(self, product_id, name=None, price=None):
        if product_id not in self.products:
            raise KeyError("Product not found.")
        if name:
            self.products[product_id]['name'] = name
        if price:
            self.products[product_id]['price'] = price
