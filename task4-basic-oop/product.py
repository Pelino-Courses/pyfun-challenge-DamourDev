class product:
    """
    A class to represent a product in inventory.

    Attributes:
        name (str): The name of the product.
        price (float): The price of the product.
        quantity (int): The quantity of the product in stock.

    Methods:
        add_inventory(quantity): Adds to the inventory of the product.
        remove_inventory(quantity): Removes from the inventory of the product.
        total_value(): Returns the total inventory value.
        display_info(): Displays the product information.

    """
    def __init__(self, name, price, quantity):
        """
        Initializes the product with name, price, and quantity.

        Args:
            name (str): The name of the product.
            price (float): The price of the product.
            quantity (int): The quantity of the product in stock.

        Raises:
            ValueError: If price or quantity is negative.
            TypeError: If name is not a string, or price and quantity are not numbers.
        """

        if not isinstance(name, str):
            raise TypeError("Name of product must be a string.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must not be negative number.")
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must not be negative number.")
        
        self.name = name
        self.price = price
        self.quantity = quantity

    def add_inventory(self, quantity):
        """
        Adds to the inventory of the product.

        Args:
            quantity (int): The quantity to add.

        Raises:
            ValueError: If quantity is negative or not an integer.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must not be a negative number.")
        self.quantity += quantity

    def remove_inventory(self, quantity):
        """
        Removes from the inventory of the product.

        Args:
            quantity (int): The quantity to remove.

        Raises:
            ValueError: If quantity is negative or not an integer.
            ValueError: If quantity to remove is greater than available stock.
        """
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Quantity must not be a negative number.")
        if quantity > self.quantity:
            raise ValueError("Cannot remove more than available stock.")
        self.quantity -= quantity
         
    def total_value(self):
        """
        Returns the total inventory value.

        Returns:
            float: The total value of the inventory.
        """
        return self.price * self.quantity
    
    def display_info(self):
        """
        Displays the product information.

        Returns:
            str: The product information.
        """
        return f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Total Value: {self.total_value()}"
    

item1 = product("Laptop", 1000, 10)
item1.add_inventory(5)
item1.remove_inventory(2)
print(item1.display_info())  