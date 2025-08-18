def factorial(n):
    """
    Calculate the factorial of a given number.
    
    Args:
        n (int): A non-negative integer
        
    Returns:
        int: The factorial of n (n!)
    """
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result


def main():
    """
    Main function to get user input and calculate factorial.
    """
    print("Simple Factorial Calculator")
    print("=" * 30)
    
    try:
        # Get input from user
        user_input = int(input("Enter a non-negative integer: "))
        
        # Calculate factorial
        result = factorial(user_input)
        
        # Display result
        if isinstance(result, str):
            print(f"Error: {result}")
        else:
            print(f"{user_input}! = {result}")
            
    except ValueError:
        print("Error: Please enter a valid integer.")
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")


# Run the program
if __name__ == "__main__":
    main()
