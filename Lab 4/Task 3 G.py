def get_student_info(student: dict) -> str:
    """
    Extracts and returns student information from a nested dictionary.
    Returns a formatted string with Full Name, Branch, and SGPA.
    """
    full_name = student.get('full_name', 'N/A')
    branch = student.get('branch', 'N/A')
    sgpa = student.get('sgpa', 'N/A')
    return f"Full Name : {full_name} , Branch : {branch} , SGPA : {sgpa}"

# Example usage:
student1 = {'full_name': 'Siddu', 'branch': 'CSE', 'sgpa': 9.0}
student2 = {'full_name': 'harsha', 'branch': 'CSM', 'sgpa': 9.2}

print(get_student_info(student1))
print(get_student_info(student2))