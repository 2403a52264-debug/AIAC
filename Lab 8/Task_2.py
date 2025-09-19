def assign_grade(score):
    # Handle invalid types
    if not isinstance(score, (int, float)):
        return "Invalid"
    
    # Handle out-of-range values
    if score < 0 or score > 100:
        return "Invalid"
    
    # Assign grades
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    else:
        return "F"


if __name__ == "__main__":
    # Test case 1
    print(f"Test case 1\n Score: 95 ->", assign_grade(95))
    # returns: A

    # Test case 2
    print(f"Test case 2 \nScore: 75 ->", assign_grade(75))
    # returns: C

    # Test case 3
    print(f"Test case 3 \nScore: -5 ->", assign_grade(-5))
    # returns: Invalid
