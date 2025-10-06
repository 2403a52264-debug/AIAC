import math

# Separate functions for each shape calculation
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    return length * width
def calculate_square_area(side):
    """Calculate the area of a square."""
    return side * side
def calculate_circle_area(radius):
    """Calculate the area of a circle."""
    return math.pi * radius * radius
# Dictionary-based dispatch system
SHAPE_CALCULATORS = {
    "rectangle": calculate_rectangle_area,
    "square": calculate_square_area,
    "circle": calculate_circle_area
}
def calculate_area(shape, x, y=0):
    """
    Calculate the area of a given shape using dictionary-based dispatch.
    
    Args:
        shape (str): The type of shape ('rectangle', 'square', 'circle')
        x (float): Primary dimension (length for rectangle, side for square, radius for circle)
        y (float): Secondary dimension for rectangle (default: 0)
    
    Returns:
        float: The calculated area
    
    Raises:
        ValueError: If the shape is not supported
    """
    if shape not in SHAPE_CALCULATORS:
        raise ValueError(f"Unsupported shape: {shape}. Supported shapes: {list(SHAPE_CALCULATORS.keys())}")
    
    calculator = SHAPE_CALCULATORS[shape]
    if shape == "rectangle":
        return calculator(x, y)
    else:
        return calculator(x)
# Example usage and testing
if __name__ == "__main__":
    # Test cases
    print("Testing shape area calculations:")
    print(f"Rectangle (5x3): {calculate_area('rectangle', 5, 3)}")
    print(f"Square (4): {calculate_area('square', 4)}")
    print(f"Circle (radius 2): {calculate_area('circle', 2):.2f}") 
    # Test error handling
    try:
        calculate_area('triangle', 3, 4)
    except ValueError as e:
        print(f"Error: {e}")
