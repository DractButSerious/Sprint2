# Create class "Drink"
class Drink:
    """
    A class for storing a drink object.

    Attributes:
        _base (str): The base of the drink (e.g., "Water", "Sprite").
        _flavors (set): A set of flavors in the drink (e.g., {"Lemon", "Cherry"}).
    """
    # Initialize the valid bases and flavors.
    _valid_bases = {"Water", "Sprite", "Coca-Cola", "Dr. Pepper", "Starry", "Root Beer"}
    _valid_flavors = {"Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", "Lime"}

    # Initialize with no base and an empty flavor list.
    def __init__(self):
        """Initializes an empty `Drink` object."""
        self._base = None
        self._flavors = set()

    # Return the _base property.
    def get_base(self):
        """
        Returns the base of the drink.

        Returns:
            str: The base of the drink.
        """
        return self._base
    
    # Return the _flavors property.
    def get_flavors(self):
        """
        Returns the flavors of the drink as a list.

        Returns:
            list: A list of the drink's flavors.
        """
        return list(self._flavors)
    
    # Return the number of flavors.
    def get_num_flavors(self):
        """
        Returns the number of flavors in the drink.

        Returns:
            int: The number of flavors.
        """
        return len(self._flavors)
    
    # Set the drink's _base property.
    def set_base(self, base):
        """
        Sets the base of the drink.

        Args:
            base (str): The new base for the drink. Valid bases are "Water", "Sprite", "Coca-Cola", "Dr. Pepper", "Starry", and "Root Beer".

        Raises:
            ValueError: If the base is invalid.
        """
        if base in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"Pick a proper base from {self._valid_bases}.")
    
    # Add a flavor to the _flavors property.
    def add_flavor(self, flavor):
        """
        Adds a flavor to the drink.

        Args:
            flavor (str): The flavor to add. Valid flavors are "Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", and "Lime".

        Raises:
            ValueError: If the flavor is invalid.
        """
        if flavor in self._valid_flavors:
            self._flavors.add(flavor)
        else:
            raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")

    # Set the _flavors property to a given list.
    def set_flavors(self, flavors):
        """
        Sets the flavors of the drink.

        Args:
            flavors (list): A list of flavors to set. Valid flavors are "Lemon", "Cherry", "Strawberry", "Mint", "Blueberry", and "Lime".

        Raises:
            ValueError: If any of the flavors are invalid.
        """
        for flavor in flavors:
            if flavor not in self._valid_flavors:
                raise ValueError(f"Pick a proper flavor from {self._valid_flavors}.")
        self._flavors = set(flavors)


# Create class "Order"
class Order:
    """
    A class representing an order of drinks.

    Attributes:
        _items (list): A list of `Drink` objects in the order.
    """
    # Give the class instance its _items property.
    def __init__(self):
        """Initializes an empty order."""
        self._items = []
    
    # Return the list of items in this instance.
    def get_items(self):
        """
        Returns a list of `Drink` objects in the order.

        Returns:
            list: A list of `Drink` objects.
        """
        return self._items

    # Return the number of items in this instance.
    def get_total(self):
        """
        Returns the total number of items in the order.

        Returns:
            int: The number of items in the order.
        """
        return len(self._items)
    
    # List out every item in the list.
    def get_receipt(self):
        """
        Generates a formatted receipt for the order.

        Returns:
            str: A formatted string representing the receipt.
        """
        receipt = "Your order receipt:\n"
        for i, drink in enumerate(self._items):
            base = drink.get_base()
            # Formats the "flavors" string like "Lemon, Mint, Blueberry"
            flavors = ", ".join(drink.get_flavors())
            # Example: "1: Base - Root Beer, Flavors - Lemon, Cherry"
            receipt += f"{i + 1}: Base - {base}, Flavors - {flavors}\n"
        return receipt
    
    # Add a Drink instance to the end of the list.
    def add_item(self, drink):
        """
        Adds a `Drink` object to the order.

        Args:
            drink (Drink): The `Drink` object to add.

        Raises:
            ValueError: If the argument is not a `Drink` object.
        """
        if isinstance(drink, Drink):
            self._items.append(drink)
        else:
            # If the instance is not a Drink, throw an error.
            raise ValueError("You can only add drinks to this order.")
    
    # Remove a Drink instance from the list based on index.
    def remove_item(self, index):
        """
        Removes a `Drink` object from the order at the specified index.

        Args:
            index (int): The index of the item to remove.

        Raises:
            IndexError: If the index is invalid.
        """
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            # If the index is outside of the list, i.e. invalid, throw an error.
            raise IndexError("Invalid index, cannot remove item.")