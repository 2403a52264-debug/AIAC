def validate_indian_mobile_number():
    """
    Function to validate Indian mobile number.
    Takes input from user and checks if:
    1. Number starts with 6, 7, 8, or 9
    2. Contains exactly 10 digits
    """
    
    # Get input from user
    mobile_number = input("Enter Indian mobile number: ")
    
    # Remove any spaces or special characters
    cleaned_number = ''.join(filter(str.isdigit, mobile_number))
    
    # Check if exactly 10 digits
    if len(cleaned_number) != 10:
        print("Invalid: Mobile number must be exactly 10 digits")
        return False
    
    # Check if starts with valid prefix (6, 7, 8, 9)
    if cleaned_number[0] not in ['6', '7', '8', '9']:
        print("Invalid: Mobile number must start with 6, 7, 8, or 9")
        return False
    
    # If all checks pass
    print("Valid Indian mobile number!")
    return True

# Run the function
if __name__ == "__main__":
    validate_indian_mobile_number()
