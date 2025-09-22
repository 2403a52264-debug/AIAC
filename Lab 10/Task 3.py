def calculate_percentage(value, percentage_rate):
    """
    Calculate the percentage of a given value.
    
    This function takes a value and a percentage rate, then calculates
    what percentage of the value the rate represents.
    
    Parameters:
    value (float or int): The base value to calculate percentage of
    percentage_rate (float or int): The percentage rate (e.g., 15 for 15%)
    
    Returns:
    float: The calculated percentage value
    
    Example:
    >>> calculate_percentage(200, 15)
    30.0
    """
    # Calculate percentage: (value * percentage_rate) / 100
    percentage_result = value * percentage_rate / 100
    return percentage_result

# Test the function with sample values
base_value = 200          # The original amount
percentage_to_calculate = 15  # 15% of the base value

# Calculate and display the result
calculated_percentage = calculate_percentage(base_value, percentage_to_calculate)
print(f"{percentage_to_calculate}% of {base_value} is: {calculated_percentage}")
