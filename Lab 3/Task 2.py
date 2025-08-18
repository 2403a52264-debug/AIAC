def sort_list(input_list, reverse=False):
    """
    Sort a list of numbers or strings in ascending or descending order.
    
    Args:
        input_list (list): List of numbers or strings to be sorted
        reverse (bool): If True, sort in descending order. If False, sort in ascending order
        
    Returns:
        list: Sorted list
        
    Raises:
        TypeError: If input is not a list
    """
    if not isinstance(input_list, list):
        raise TypeError("Input must be a list")
    
    return sorted(input_list, reverse=reverse)


def get_user_input():
    """
    Get a list from user input.
    
    Returns:
        list: User's input list
    """
    print("Enter elements separated by spaces (e.g., 5 2 8 1 9):")
    try:
        user_input = input("Enter your list: ").strip()
        if not user_input:
            return []
        
        # Try to convert to numbers first, fall back to strings
        elements = user_input.split()
        try:
            # Try to convert to integers
            return [int(x) for x in elements]
        except ValueError:
            try:
                # Try to convert to floats
                return [float(x) for x in elements]
            except ValueError:
                # Keep as strings
                return elements
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        exit()


def display_sorting_demo():
    """
    Demonstrate sorting with clear input and output examples.
    """
    print("Python Sorting Function Demo")
    print("=" * 40)
    
    # Example 1: Numbers in ascending order
    print("\nExample 1: Sorting numbers in ascending order")
    print("-" * 45)
    numbers = [64, 34, 25, 12, 22, 11, 90]
    print(f"Input:  {numbers}")
    sorted_numbers = sort_list(numbers)
    print(f"Output: {sorted_numbers}")
    
    # Example 2: Numbers in descending order
    print("\nExample 2: Sorting numbers in descending order")
    print("-" * 45)
    print(f"Input:  {numbers}")
    sorted_numbers_desc = sort_list(numbers, reverse=True)
    print(f"Output: {sorted_numbers_desc}")
    
    # Example 3: Strings
    print("\nExample 3: Sorting strings")
    print("-" * 30)
    words = ["banana", "apple", "cherry", "date", "blueberry"]
    print(f"Input:  {words}")
    sorted_words = sort_list(words)
    print(f"Output: {sorted_words}")
    
    # Example 4: Mixed data types
    print("\nExample 4: Sorting mixed data (strings)")
    print("-" * 40)
    mixed = ["zebra", "123", "apple", "45", "cat"]
    print(f"Input:  {mixed}")
    sorted_mixed = sort_list(mixed)
    print(f"Output: {sorted_mixed}")


def main():
    """
    Main function to run the sorting demonstration.
    """
    # Display demo examples
    display_sorting_demo()
    
    # Interactive user input
    print("\n" + "=" * 40)
    print("Interactive Sorting")
    print("=" * 40)
    
    try:
        # Get user input
        user_list = get_user_input()
        
        if not user_list:
            print("No input provided.")
            return
        
        print(f"\nYour input: {user_list}")
        
        # Sort in ascending order
        ascending = sort_list(user_list)
        print(f"Ascending:  {ascending}")
        
        # Sort in descending order
        descending = sort_list(user_list, reverse=True)
        print(f"Descending: {descending}")
        
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
