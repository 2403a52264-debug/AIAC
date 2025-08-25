def calculate_factorial():
    """
    Function to calculate factorial of a given number.
    Takes input from user and calculates factorial.
    Handles negative numbers with appropriate error message.
    """
    
    # Get input from user
    try:
        number = int(input("Enter a number to calculate factorial: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return
    
    # Check if number is negative
    if number < 0:
        print("Error: Factorial is not defined for negative numbers!")
        return
    
    # Calculate factorial
    if number == 0 or number == 1:
        factorial = 1
    else:
        factorial = 1
        for i in range(2, number + 1):
            factorial *= i
    
    # Display result
    print(f"{number}! = {factorial}")

# Run the function
if __name__ == "__main__":
    calculate_factorial()
