def calculate_factorial(n):
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


def get_user_input():
    """
    Get a valid integer input from the user.
    
    Returns:
        int: The user's input number
    """
    while True:
        try:
            user_input = int(input("Enter a non-negative integer to calculate factorial: "))
            if user_input < 0:
                print("Error: Please enter a non-negative integer.")
                continue
            return user_input
        except ValueError:
            print("Error: Please enter a valid integer.")
        except KeyboardInterrupt:
            print("\nProgram terminated by user.")
            exit()


def main():
    """
    Main function to run the factorial calculator.
    """
    print("Factorial Calculator")
    print("=" * 25)
    
    try:
        # Get input from user
        number = get_user_input()
        
        # Calculate factorial
        result = calculate_factorial(number)
        
        # Display result
        print(f"\nThe factorial of {number} is: {result}")
        print(f"Mathematical notation: {number}! = {result}")
        
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the program
if __name__ == "__main__":
    main()
