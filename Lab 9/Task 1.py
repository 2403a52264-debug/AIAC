def sum_even_odd(numbers):
    """
    Calculate the sum of even and odd numbers in a list.

    Args:
        numbers (list of int): List of integers to process.

    Returns:
        tuple: (sum of even numbers, sum of odd numbers)
    """
    # Initialize sums for even and odd numbers
    even_sum = 0
    odd_sum = 0
    # Iterate through each number in the list
    for num in numbers:
        if num % 2 == 0:  # Check if the number is even
            even_sum += num
        else:
            odd_sum += num #check if the number is odd
     # Return the sums as a tuple (even_sum, odd_sum)
    return even_sum, odd_sum
# Define a list of numbers to process
numbers = [11,12,13, 14, 15, 16]
# Call the function and store the returned sums
even_sum, odd_sum = sum_even_odd(numbers)
# Print the sum of even numbers
print("Sum of even numbers:", even_sum)
# Print the sum of odd numbers
print("Sum of odd numbers:", odd_sum)