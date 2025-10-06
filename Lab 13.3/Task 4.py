# Old way (inefficient)
numbers = [1, 2, 3, 4, 5]
squares_old = []
for num in numbers:
    squares_old.append(num * num)

# New way (list comprehension)
squares_new = [num * num for num in numbers]

print("Numbers:", numbers)
print("Squares (old):", squares_old)
print("Squares (new):", squares_new)
