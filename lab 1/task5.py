# Python program to count number of lines in a file

# Ask user for the file name
file_name = input("Enter the file name: ")

try:
    # Open the file in read mode
    with open(file_name, "r") as file:
        # Read all lines into a list
        lines = file.readlines()

        # Count number of lines
        num_lines = len(lines)

    print(f"Number of lines in '{file_name}': {num_lines}")

except FileNotFoundError:
    print(f"Error: File '{file_name}' not found.")
except Exception as e:
    print(f"An error occurred: {e}")
