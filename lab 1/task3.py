def reverse_string(s):
    return s[::-1]

user_input = input("Enter a string to reverse: ")
reversed_str = reverse_string(user_input)
print("Reversed string:", reversed_str)