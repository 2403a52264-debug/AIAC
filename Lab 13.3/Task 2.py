def read_file(filename):
    """
    Read the contents of a file using modern Python practices.
    
    Args:
        filename (str): The path to the file to read
        
    Returns:
        str: The contents of the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If permission is denied to read the file
        UnicodeDecodeError: If the file contains invalid characters
        OSError: For other file system related errors
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = file.read()
            return data
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found. Please check the file path.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read file '{filename}'. Check file permissions.")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Unable to decode file '{filename}'. The file may contain invalid characters.")
    except OSError as e:
        raise OSError(f"Error reading file '{filename}': {e}")

def read_file_lines(filename):
    """
    Read the contents of a file line by line using modern Python practices.
    
    Args:
        filename (str): The path to the file to read
        
    Returns:
        list: A list of lines from the file
        
    Raises:
        FileNotFoundError: If the file doesn't exist
        PermissionError: If permission is denied to read the file
        UnicodeDecodeError: If the file contains invalid characters
        OSError: For other file system related errors
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            lines = file.readlines()
            # Remove trailing newlines from each line
            return [line.rstrip('\n') for line in lines]
    except FileNotFoundError:
        raise FileNotFoundError(f"File '{filename}' not found. Please check the file path.")
    except PermissionError:
        raise PermissionError(f"Permission denied to read file '{filename}'. Check file permissions.")
    except UnicodeDecodeError as e:
        raise UnicodeDecodeError(f"Unable to decode file '{filename}'. The file may contain invalid characters.")
    except OSError as e:
        raise OSError(f"Error reading file '{filename}': {e}")

def write_file(filename, content):
    """
    Write content to a file using modern Python practices.
    
    Args:
        filename (str): The path to the file to write
        content (str): The content to write to the file
        
    Raises:
        PermissionError: If permission is denied to write the file
        OSError: For other file system related errors
    """
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)
    except PermissionError:
        raise PermissionError(f"Permission denied to write file '{filename}'. Check file permissions.")
    except OSError as e:
        raise OSError(f"Error writing file '{filename}': {e}")

# Example usage and testing
if __name__ == "__main__":
    # Test reading a file
    try:
        # Create a test file
        test_content = "Hello, World!\nThis is a test file.\nLine 3"
        write_file("test_file.txt", test_content)
        
        # Read the file
        content = read_file("test_file.txt")
        print("File content:")
        print(content)
        
        # Read file as lines
        lines = read_file_lines("test_file.txt")
        print("\nFile lines:")
        for i, line in enumerate(lines, 1):
            print(f"Line {i}: {line}")
            
    except Exception as e:
        print(f"Error: {e}")
    
    # Test error handling
    print("\nTesting error handling:")
    try:
        read_file("nonexistent_file.txt")
    except FileNotFoundError as e:
        print(f"Expected error: {e}")
