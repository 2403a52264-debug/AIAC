def bubble_sort(arr):
    """
    Simple Bubble Sort implementation
    """
    n = len(arr)
    
    # Outer loop for passes
    for i in range(n):
        # Inner loop for comparisons
        for j in range(0, n - i - 1):
            # Swap if current element is greater than next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr


# Test the function
if __name__ == "__main__":
    # Test array
    numbers = [64, 34, 25, 12, 22, 11, 90, 5]
    
    print("Original array:", numbers)
    
    # Sort the array
    sorted_numbers = bubble_sort(numbers.copy())  # Use copy to preserve original
    
    print("Sorted array: ", sorted_numbers)
    
    # Verify it's sorted
    is_sorted = all(sorted_numbers[i] <= sorted_numbers[i+1] for i in range(len(sorted_numbers)-1))
    print("Is sorted:", is_sorted)