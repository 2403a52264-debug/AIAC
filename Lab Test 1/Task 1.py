def Age_Classifies(age):
    if age < 0:
        return "Invalid age"
    elif age <= 12:
        return "Child"
    elif age <= 19:
        return "Teen"
    elif age <= 59:
        return "Adult"
    else:
        return "Senior"

# Example usage:
age = int(input("Enter age: "))
print("Age group:", Age_Classifies(age))