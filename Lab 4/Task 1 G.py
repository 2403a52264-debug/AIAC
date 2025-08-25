def is_valid_indian_mobile(number: str) -> bool:
    """
    Validates if the input is a valid Indian mobile number.
    - Starts with 6, 7, 8, or 9
    - Contains exactly 10 digits
    """
    return (
        len(number) == 10 and
        number.isdigit() and
        number[0] in {'6', '7', '8', '9'}
    )

# Example usage:
mobile = input("Enter mobile number: ")
if is_valid_indian_mobile(mobile):
    print("Valid Indian mobile number.")
else:
    print("Invalid Indian mobile number.")