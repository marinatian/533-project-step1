# sales.py

class SalesManager:
    """
    SalesManager class is used to record and manage sales data.

    Attributes:
        sales_records (list): A list to store sales data as dictionaries.

    Methods:
        __init__(): Initializes an empty sales_records list.
        record_sale(product_id, quantity, price): Records a sale by adding a dictionary to sales_records.
        total_sales(): Calculates and returns the total sales revenue.
    """
    def __init__(self):
        """Initializes a SalesManager object with an empty sales_records list."""
        self.sales_records = []

    def record_sale(self, product_id, quantity, price):
        """
        Records a sale by adding a dictionary to the sales_records list.

        Args:
            product_id (str): The unique identifier for the product being sold.
            quantity (int): The quantity of the product sold.
            price (float): The price per unit of the product.

        Returns:
            None
        """
        self.sales_records.append({"product_id": product_id, "quantity": quantity, "price": price})

    def total_sales(self):
        """
        Calculates and returns the total sales revenue.

        Returns:
            float: The total sales revenue calculated as the sum of (price * quantity) for all sales records.
        """
        return sum(record['price'] * record['quantity'] for record in self.sales_records)
