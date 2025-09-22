def calculate_grade_with_elif(score):
    """
    Calculate letter grade using elif statements for cleaner logic.
    
    Parameters:
    score (int or float): The numerical score to convert to letter grade
    
    Returns:
    str: Letter grade (A, B, C, D, or F)
    
    Grade Scale:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: 0-59
    """
    # Validate input
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    
    # Clean logic using elif statements
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_grade_with_dictionary(score):
    """
    Calculate letter grade using dictionary mapping for efficient lookup.
    
    Parameters:
    score (int or float): The numerical score to convert to letter grade
    
    Returns:
    str: Letter grade (A, B, C, D, or F)
    
    Grade Scale:
    - A: 90-100
    - B: 80-89
    - C: 70-79
    - D: 60-69
    - F: 0-59
    """
    # Validate input
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    
    # Dictionary mapping for grade ranges
    grade_ranges = {
        range(90, 101): "A",
        range(80, 90): "B",
        range(70, 80): "C",
        range(60, 70): "D",
        range(0, 60): "F"
    }
    
    # Find the appropriate grade using dictionary lookup
    for score_range, grade in grade_ranges.items():
        if score in score_range:
            return grade


def calculate_grade_with_list_comprehension(score):
    """
    Calculate letter grade using list comprehension and zip for compact logic.
    
    Parameters:
    score (int or float): The numerical score to convert to letter grade
    
    Returns:
    str: Letter grade (A, B, C, D, or F)
    """
    # Validate input
    if not isinstance(score, (int, float)):
        raise TypeError("Score must be a number")
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100")
    
    # Define grade boundaries and corresponding letters
    grade_boundaries = [90, 80, 70, 60, 0]
    grade_letters = ["A", "B", "C", "D", "F"]
    
    # Use list comprehension to find the first boundary that score meets
    grade_index = next(i for i, boundary in enumerate(grade_boundaries) if score >= boundary)
    return grade_letters[grade_index]


def display_grade_comparison():
    """
    Display a comparison of different grade calculation methods.
    """
    print("=== Grade Calculation Methods Comparison ===")
    print("Score\telif Method\tDictionary\tList Comp")
    print("-" * 50)
    
    test_scores = [95, 85, 75, 65, 55, 45]
    
    for score in test_scores:
        grade_elif = calculate_grade_with_elif(score)
        grade_dict = calculate_grade_with_dictionary(score)
        grade_list = calculate_grade_with_list_comprehension(score)
        
        print(f"{score}\t{grade_elif}\t\t{grade_dict}\t\t{grade_list}")


def get_student_grade_report():
    """
    Interactive function to get grade report for multiple students.
    """
    print("\n=== Student Grade Report System ===")
    
    students_data = []
    
    # Collect student data
    while True:
        student_name = input("Enter student name (or 'quit' to finish): ").strip()
        if student_name.lower() == 'quit':
            break
            
        try:
            score = float(input(f"Enter {student_name}'s score (0-100): "))
            grade = calculate_grade_with_elif(score)
            
            students_data.append({
                'name': student_name,
                'score': score,
                'grade': grade
            })
            
            print(f"✓ {student_name}: {score}% -> Grade {grade}\n")
            
        except ValueError:
            print("Invalid score. Please enter a number between 0 and 100.\n")
        except (TypeError, ValueError) as e:
            print(f"Error: {e}\n")
    
    # Display summary report
    if students_data:
        print("\n" + "=" * 50)
        print("STUDENT GRADE SUMMARY")
        print("=" * 50)
        print(f"{'Student Name':<20} {'Score':<8} {'Grade':<6}")
        print("-" * 50)
        
        for student in students_data:
            print(f"{student['name']:<20} {student['score']:<8.1f} {student['grade']:<6}")
        
        # Calculate statistics
        total_students = len(students_data)
        average_score = sum(student['score'] for student in students_data) / total_students
        grade_counts = {}
        
        for student in students_data:
            grade_counts[student['grade']] = grade_counts.get(student['grade'], 0) + 1
        
        print(f"\nTotal Students: {total_students}")
        print(f"Average Score: {average_score:.1f}%")
        print("Grade Distribution:")
        for grade in ['A', 'B', 'C', 'D', 'F']:
            count = grade_counts.get(grade, 0)
            print(f"  Grade {grade}: {count} students")


def main():
    """
    Main function to demonstrate different grade calculation methods.
    """
    # Demonstrate all three methods with sample scores
    display_grade_comparison()
    
    # Interactive student grade system
    get_student_grade_report()


# Run the main function if this script is executed directly
if __name__ == "__main__":
    main()
