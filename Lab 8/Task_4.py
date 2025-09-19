class ShoppingCart:
    def __init__(self):
        self.items = {}  # store items as {name: price}

    def add_item(self, name, price):
        self.items[name] = price
        return f"Added {name} for {price}"

    def remove_item(self, name):
        if name in self.items:
            del self.items[name]
            return f"Removed {name}"
        return f"{name} not found"

    def total_cost(self):
        return sum(self.items.values())

if __name__ == "__main__":
    cart = ShoppingCart()

    # Test case 1
    print("Test case 1 \n", cart.add_item("Apple", 30))
    # returns: Added Apple for 30

    # Test case 2
    print("Test case 2 \n", cart.add_item("Banana", 10))
    # returns: Added Banana for 10

    # Test case 3
    print("Test case 3 \n", cart.total_cost())
    # returns: 40
