def calc_average(marks):
    """
    Calculate the average of a list of marks.
    
    This function takes a list of numerical marks and returns
    the average (mean) of all the marks.
    
    Parameters:
    marks (list): A list of numerical values representing marks
    
    Returns:
    float: The average of all marks
    
    Raises:
    ZeroDivisionError: If the marks list is empty
    TypeError: If marks contains non-numeric values
    
    Example:
    >>> calc_average([85, 90, 78, 92])
    86.25
    """
    # Validate input
    if not marks:
        raise ValueError("Marks list cannot be empty")
    
    total = 0
    for m in marks:
        total += m
    average = total / len(marks)
    return average  # Fixed: was 'avrage' (typo)

# Test the function
marks = [85, 90, 78, 92]
print("Average Score is", calc_average(marks))  # Fixed: missing closing parenthesis

# Expected Output: Average Score is 86.25
