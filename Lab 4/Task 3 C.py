def student_information():
    """
    Function that represents student information using nested dictionaries.
    Extracts and displays Full Name, Branch, and SGPA for each student.
    """
    
    # Nested dictionary representing student information
    students = {
        "student1": {
            "Full Name": "Siddu",
            "Branch": "CSE",
            "SGPA": 9.0
        },
        "student2": {
            "Full Name": "harsha",
            "Branch": "CSM",
            "SGPA": 9.2
        }
    }
    
    # Extract and display information for each student
    print("Student Information:")
    print("=" * 30)
    
    for student_id, student_data in students.items():
        print(f"Example {student_id[-1]}: Full Name : {student_data['Full Name']} , Branch : {student_data['Branch']} , SGPA : {student_data['SGPA']}")
    
    return students

# Alternative function that takes student data as input
def create_student_dictionary():
    """
    Function to create student dictionary by taking input from user.
    """
    
    students = {}
    student_count = 1
    
    while True:
        print(f"\nEnter details for Student {student_count}:")
        
        # Get student information
        full_name = input("Enter Full Name: ")
        branch = input("Enter Branch: ")
        
        try:
            sgpa = float(input("Enter SGPA: "))
        except ValueError:
            print("Invalid SGPA! Please enter a valid number.")
            continue
        
        # Create student dictionary
        student_data = {
            "Full Name": full_name,
            "Branch": branch,
            "SGPA": sgpa
        }
        
        students[f"student{student_count}"] = student_data
        
        # Display the student information
        print(f"Example {student_count}: Full Name : {full_name} , Branch : {branch} , SGPA : {sgpa}")
        
        # Ask if user wants to add more students
        add_more = input("\nDo you want to add another student? (yes/no): ").lower()
        if add_more not in ['yes', 'y']:
            break
        
        student_count += 1
    
    return students

# Run the functions
if __name__ == "__main__":
    print("Method 1: Pre-defined student information")
    print("-" * 40)
    student_information()
    
    print("\n" + "=" * 50)
    print("Method 2: Interactive student input")
    print("-" * 40)
    create_student_dictionary()
