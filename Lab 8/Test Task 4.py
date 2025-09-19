from Task_4 import ShoppingCart

if __name__ == "__main__":
    cart = ShoppingCart()

    # Test case 1
    print("Test case 1 \n", cart.add_item("Apple", 30))      
    # returns: Added Apple for 30

    # Test case 2
    print("Test case 2 \n", cart.add_item("Banana", 10))      
    # returns: Added Banana for 10

    # Test case 3
    print("Test case 3 \n", cart.add_item("Milk", 50))       
    # returns: Added Milk for 50

    # Test case 4
    print("Test case 4 \n", cart.total_cost())               
    # returns: 90

    # Test case 5
    print("Test case 5 \n", cart.remove_item("Banana"))      
    # returns: Removed Banana

    # Test case 6
    print("Test case 6 \n", cart.total_cost())               
    # returns: 80

    # Test case 7
    print("Test case 7 \n", cart.remove_item("Orange"))      
    # returns: Orange not found

    # Test case 8
    print("Test case 8 \n", cart.add_item("Eggs", 60))       
    # returns: Added Eggs for 60

    # Test case 9
    print("Test case 9 \n", cart.total_cost())               
    # returns: 140

    # Test case 10
    print("Test case 10 \n", cart.remove_item("Apple"))      
    # returns: Removed Apple

    # Test case 11
    print("Test case 11 \n", cart.total_cost())              
    # returns: 110
