def fibonacci_sequence(n):
    """
    Returns the Fibonacci sequence as a list up to n terms.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Example usage:
n = int(input("Enter the number of terms for the Fibonacci sequence: "))
print(fibonacci_sequence(n)