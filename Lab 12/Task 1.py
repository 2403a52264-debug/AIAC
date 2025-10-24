def linear_search(arr, target):
    """
    Performs linear search on a list to find the target value.
    
    Args:
        arr (list): The list to search in
        target: The value to search for
    
    Returns:
        int: The index of the target value if found, -1 if not found
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


# Example usage and test cases
if __name__ == "__main__":
    # Test case 1: Value found
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90]
    target = 50
    result = linear_search(numbers, target)
    print(f"Searching for {target} in {numbers}")
    if result != -1:
        print(f"Found {target} at index {result}")
    else:
        print(f"{target} not found in the list")
    
    print("-" * 40)
    
    # Test case 2: Value not found
    target2 = 25
    result2 = linear_search(numbers, target2)
    print(f"Searching for {target2} in {numbers}")
    if result2 != -1:
        print(f"Found {target2} at index {result2}")
    else:
        print(f"{target2} not found in the list")
    
    print("-" * 40)
    
    # Test case 3: Empty list
    empty_list = []
    result3 = linear_search(empty_list, 10)
    print(f"Searching for 10 in empty list: {result3}")
    
    print("-" * 40)
    
    # Test case 4: String list
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    target_name = "Charlie"
    result4 = linear_search(names, target_name)
    print(f"Searching for '{target_name}' in {names}")
    if result4 != -1:
        print(f"Found '{target_name}' at index {result4}")
    else:
        print(f"'{target_name}' not found in the list")
