def area_of_rect(L, B):
    """
    Calculate the area of a rectangle.
    
    This function takes the length and breadth of a rectangle and returns
    the area by multiplying these two dimensions.
    
    Parameters:
    L (float or int): Length of the rectangle
    B (float or int): Breadth (width) of the rectangle
    
    Returns:
    float or int: The area of the rectangle (L * B)
    
    Raises:
    TypeError: If L or B are not numeric values
    ValueError: If L or B are negative numbers
    
    Example:
    >>> area_of_rect(10, 20)
    200
    """
    # Validate input types
    if not isinstance(L, (int, float)):
        raise TypeError(f"Length must be a number, got {type(L).__name__}")
    if not isinstance(B, (int, float)):
        raise TypeError(f"Breadth must be a number, got {type(B).__name__}")
    
    # Validate input values
    if L < 0:
        raise ValueError("Length cannot be negative")
    if B < 0:
        raise ValueError("Breadth cannot be negative")
    return L * B  # Return the product of length and breadth
# Test the function with sample values
print(area_of_rect(10,20))  # Output: 200
