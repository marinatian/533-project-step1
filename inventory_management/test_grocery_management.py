from products import ProductManager
from stock import StockManager, PerishableStockManager
import datetime

product_manager = ProductManager()
stock_manager = StockManager()
perishable_stock_manager = PerishableStockManager()

def str_to_date(date_str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d').date()

product_manager.add_product('P001', 'Milk', 1.99)
product_manager.add_product('P002', 'Bread', 2.49)
print("Added Milk and Bread to the products.")

product_manager.update_product('P002', price=2.99)
print("Updated Bread price to $2.99.")

try:
    product_manager.remove_product('P003')
except KeyError as e:
    print(f"Failed to remove product: {e}")

stock_manager.add_stock('P001', 100)  
stock_manager.add_stock('P002', 50) 
print("Added stock for Milk and Bread.")

perishable_stock_manager.add_perishable_stock('P001', 50, str_to_date('2023-12-01'))
print("Added perishable stock for Milk with expiry date 2023-12-01.")

try:
    stock_manager.remove_stock('P002', 10)
    print("Sold 10 units of Bread.")
except ValueError as e:
    print(f"Failed to remove stock: {e}")

today = datetime.date.today()
expired_stock = perishable_stock_manager.check_expiry(today)
print(f"Expired stock as of {today}: {expired_stock}")
perishable_stock_manager.remove_expired_stock(today)
print("Removed expired perishable stock.")

print("\nFinal products and stock list:")
for product_id, product_info in product_manager.products.items():
    stock_info = stock_manager.stock.get(product_id, 0)
    perishable_info = perishable_stock_manager.perishable_stock.get(product_id, [])
    print(f"Product ID: {product_id}, Name: {product_info['name']}, Price: {product_info['price']}, Stock: {stock_info}, Perishable Stock: {perishable_info}")
