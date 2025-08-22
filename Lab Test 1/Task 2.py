class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks

    def display(self):
        print("Student class:", self.__class__)
        print("Details of the student:")
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

if __name__ == "__main__":
    name = input("Enter student name: ").strip()
    roll_no = input("Enter roll number: ").strip()
    marks = float(input("Enter marks: ").strip())

    student = Student(name, roll_no, marks)
    student.display()