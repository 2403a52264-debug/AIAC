class student:
    pass
student = student()
student.name = input("Enter Student Name: ")
student.rollno = int(input("Enter Roll NO: "))
student.marks = int(input("Enter Marks:"))
if student.marks >= 90:
    student.grade = "A"
elif student.marks >= 75:
    student.grade = "B"
elif student.marks >= 60:
    student.grade = "C"
else :
    student.grade = "Fail"
print("\n---Student Details---\n")
print("Name:",student.name)
print("Roll NO:",student.rollno)
print("Marks:",student.marks)
print("Grade:",student.grade)