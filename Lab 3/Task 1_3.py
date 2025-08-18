def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n == 0 or n == 1:
        return 1
    
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
def factorial_recursive(n):
    """
    Calculate factorial using recursive approach.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n (n!)
        
    Raises:
        ValueError: If n is negative
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")   
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
def main():
    """
    Main function to demonstrate factorial calculations.
    """
    print("Python Function to Calculate Factorial")
    print("=" * 40)
    # Test cases
    test_numbers = [0, 1, 5, 10]
    print("\nTesting factorial function:")
    print("-" * 30)
    for num in test_numbers:
        try:
            result = factorial(num)
            print(f"{num}! = {result}")
        except ValueError as e:
            print(f"Error for {num}: {e}")
    print("\nTesting recursive factorial function:")
    print("-" * 40)
    for num in test_numbers:
        try:
            result = factorial_recursive(num)
            print(f"{num}! = {result}")
        except ValueError as e:
            print(f"Error for {num}: {e}")
    print("\n" + "=" * 40)
    print("Interactive Testing")
    print("=" * 40)
    try:
        user_input = int(input("Enter a number to calculate factorial: "))
        result = factorial(user_input)
        print(f"{user_input}! = {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


if __name__ == "__main__":
    main()