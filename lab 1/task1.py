def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Optional: ignore case and spaces
    return s == s[::-1]

# Example usage:
string = input("Enter a string to check if it is a palindrome: ")
print(is_palindrome(string))