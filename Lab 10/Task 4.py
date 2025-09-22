def create_student_list():
    """
    Create and return a list of student names.
    
    Returns:
    list: A list containing student names
    """
    student_names = ["Alice", "Bob", "Charlie"]
    return student_names


def welcome_single_student(student_name):
    """
    Generate a welcome message for a single student.
    
    Parameters:
    student_name (str): The name of the student to welcome
    
    Returns:
    str: A formatted welcome message
    """
    welcome_message = f"Welcome, {student_name}!"
    return welcome_message


def welcome_all_students(student_list):
    """
    Generate welcome messages for all students in the list.
    
    Parameters:
    student_list (list): A list of student names
    
    Returns:
    list: A list of welcome messages for each student
    """
    welcome_messages = []
    for student_name in student_list:
        message = welcome_single_student(student_name)
        welcome_messages.append(message)
    return welcome_messages


def display_welcome_messages(student_list):
    """
    Display welcome messages for all students.
    
    Parameters:
    student_list (list): A list of student names
    """
    print("=== Student Welcome System ===")
    welcome_messages = welcome_all_students(student_list)
    
    for message in welcome_messages:
        print(message)
    
    print(f"\nTotal students welcomed: {len(student_list)}")


def add_student_to_list(student_list, new_student_name):
    """
    Add a new student to the existing student list.
    
    Parameters:
    student_list (list): The current list of students
    new_student_name (str): Name of the new student to add
    
    Returns:
    list: Updated student list with the new student
    """
    if new_student_name not in student_list:
        student_list.append(new_student_name)
        print(f"Successfully added {new_student_name} to the student list.")
    else:
        print(f"{new_student_name} is already in the student list.")
    
    return student_list


def remove_student_from_list(student_list, student_name):
    """
    Remove a student from the student list.
    
    Parameters:
    student_list (list): The current list of students
    student_name (str): Name of the student to remove
    
    Returns:
    list: Updated student list without the specified student
    """
    if student_name in student_list:
        student_list.remove(student_name)
        print(f"Successfully removed {student_name} from the student list.")
    else:
        print(f"{student_name} is not found in the student list.")
    
    return student_list


def main():
    """
    Main function to demonstrate the student management system.
    """
    # Create initial student list
    students = create_student_list()
    
    # Display welcome messages for all students
    display_welcome_messages(students)
    
    # Demonstrate adding a new student
    print("\n" + "="*40)
    print("Adding a new student...")
    students = add_student_to_list(students, "Diana")
    
    # Display updated welcome messages
    print("\nUpdated welcome messages:")
    display_welcome_messages(students)
    
    # Demonstrate removing a student
    print("\n" + "="*40)
    print("Removing a student...")
    students = remove_student_from_list(students, "Bob")
    
    # Display final welcome messages
    print("\nFinal welcome messages:")
    display_welcome_messages(students)


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
