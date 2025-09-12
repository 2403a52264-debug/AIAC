class SRU_Student:
    """
    Represents a student at SRU University.

    Attributes:
        name (str): The student's name.
        roll_no (int): The student's roll number.
        hostel_status (str): "Hosteller" or "Day Scholar".
        fee (int): The total fee paid by the student.
    """

    def __init__(self, name, roll_no, hostel_status):
        """
        Initialize the SRU_Student object with name, roll number, and hostel status.

        Args:
            name (str): Student's name.
            roll_no (int): Student's roll number.
            hostel_status (str): Hostel status ("Hosteller" or "Day Scholar").
        """
        self.name = name  # Store student's name
        self.roll_no = roll_no  # Store student's roll number
        self.hostel_status = hostel_status  # Store hostel status
        self.fee = 0  # Initialize fee to 0

    def fee_update(self, amount):
        """
        Update the fee paid by the student.

        Args:
            amount (int): Amount to add to the fee.
        """
        self.fee += amount  # Add the amount to the current fee

    def display_details(self):
        """
        Display the student's details.
        """
        print("---- Student Details ----")
        print("Name:", self.name)  # Print student's name
        print("Roll No:", self.roll_no)  # Print student's roll number
        print("Hostel Status:", self.hostel_status)  # Print hostel status
        print("Fee Paid:", self.fee)  # Print total fee paid

# Take input from the user for student details
name = input("Enter student name: ")
roll_no = int(input("Enter roll number: "))
hostel_status = input("Enter hostel status (Hosteller/Day Scholar): ")

# Create SRU_Student object with user input
student1 = SRU_Student(name, roll_no, hostel_status)

# Take input for fee update
fee_amount = int(input("Enter fee amount to update: "))
student1.fee_update(fee_amount)

# Display student details
student1.display_details()