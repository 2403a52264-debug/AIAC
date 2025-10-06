class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def get_average(self):
        return sum(self.marks) / len(self.marks)
    
    def get_grade(self):
        avg = self.get_average()
        if avg >= 90: return "A"
        elif avg >= 80: return "B"
        elif avg >= 70: return "C"
        elif avg >= 60: return "D"
        else: return "F"
    
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Marks: {self.marks}")
        print(f"Average: {self.get_average():.1f}")
        print(f"Grade: {self.get_grade()}")


# Simple example
if __name__ == "__main__":
    student = Student("John", 20, [85, 90, 78, 92])
    student.display_info()
