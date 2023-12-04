# discounts.py

class DiscountManager:
    """
    DiscountManager class is used to manage discounts for products.

    Attributes:
        discounts (dict): A dictionary to store product-specific discount rates.

    Methods:
        __init__(): Initializes an empty discounts dictionary.
        add_discount(product_id, discount_rate): Adds a discount for a specific product.
        remove_discount(product_id): Removes a discount for a specific product.
        apply_discount(product_id, price): Applies a discount to the price of a product.
    """
    def __init__(self):
        """Initializes a DiscountManager object with an empty discounts dictionary."""
        self.discounts = {}

    def add_discount(self, product_id, discount_rate):
        """
        Adds a discount for a specific product.

        Args:
            product_id (str): The unique identifier for the product to apply the discount to.
            discount_rate (float): The discount rate as a decimal (e.g., 0.2 for 20% off).

        Raises:
            ValueError: If the discount rate is not between 0 and 1.
        """
        if not 0 <= discount_rate <= 1:
            raise ValueError("Discount rate must be between 0 and 1.")
        self.discounts[product_id] = discount_rate

    def remove_discount(self, product_id):
        """
        Removes a discount for a specific product.

        Args:
            product_id (str): The unique identifier for the product to remove the discount from.

        Raises:
            KeyError: If no discount is found for the specified product ID.
        """
        if product_id not in self.discounts:
            raise KeyError(f"No discount found for product ID {product_id}.")
        del self.discounts[product_id]

    def apply_discount(self, product_id, price):
        """
        Applies a discount to the price of a product.

        Args:
            product_id (str): The unique identifier for the product to apply the discount to.
            price (float): The original price of the product.

        Returns:
            float: The discounted price after applying the discount (or the original price if no discount is found).
        """
        if product_id not in self.discounts:
            return price
        return price * (1 - self.discounts[product_id])
