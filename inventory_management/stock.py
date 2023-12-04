# stock.py

class StockManager:
    def __init__(self):
        self.stock = {}

    def add_stock(self, product_id, quantity):
        self.stock[product_id] = self.stock.get(product_id, 0) + quantity

    def remove_stock(self, product_id, quantity):
        if product_id not in self.stock or self.stock[product_id] < quantity:
            raise ValueError("Insufficient stock.")
        self.stock[product_id] -= quantity

class PerishableStockManager(StockManager):
    def __init__(self):
        super().__init__()
        self.perishable_stock = {}

    def add_perishable_stock(self, product_id, quantity, expiry_date):
        super().add_stock(product_id, quantity)
        if product_id not in self.perishable_stock:
            self.perishable_stock[product_id] = []
        self.perishable_stock[product_id].append({'quantity': quantity, 'expiry_date': expiry_date})

    def check_expiry(self, current_date):
        expired_items = {}
        for product_id, stock_items in self.perishable_stock.items():
            expired_items[product_id] = sum(item['quantity'] for item in stock_items if item['expiry_date'] < current_date)
        return expired_items

    def remove_expired_stock(self, current_date):
        for product_id, stock_items in list(self.perishable_stock.items()):
            self.perishable_stock[product_id] = [item for item in stock_items if item['expiry_date'] >= current_date]
            if not self.perishable_stock[product_id]:
                del self.perishable_stock[product_id]
                self.stock[product_id] = 0
