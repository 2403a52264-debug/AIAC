def add(a, b):
    """
    Return the sum of a and b.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b  # Add the two numbers

def subtract(a, b):
    """
    Return the difference of a and b.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The difference of a and b.
    """
    return a - b  # Subtract b from a

def multiply(a, b):
    """
    Return the product of a and b.

    Args:
        a (float): First number.
        b (float): Second number.

    Returns:
        float: The product of a and b.
    """
    return a * b  # Multiply the two numbers

def divide(a, b):
    """
    Return the division of a by b.

    Args:
        a (float): Numerator.
        b (float): Denominator.

    Returns:
        float: The result of division.

    Raises:
        ZeroDivisionError: If b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")  # Handle division by zero
    return a / b  # Divide a by b

if __name__ == "__main__":
    # Take input from the user
    a = float(input("Enter first number: "))  # Input first number
    b = float(input("Enter second number: "))  # Input second number

    print("Add: ", add(a, b))  # Print sum
    print("Subtract: ", subtract(a, b))  # Print difference
    print("Multiply: ", multiply(a, b))  # Print product
    print("Divide: ", divide(a, b))  # Print division result

