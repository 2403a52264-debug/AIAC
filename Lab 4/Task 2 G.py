def factorial(n: int) -> int:
    """
    Calculates the factorial of a non-negative integer n.
    Returns None if n is negative.
    """
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage:
num = int(input("Enter a number: "))
fact = factorial(num)
if fact is not None:
    print(f"{num}! = {fact}")