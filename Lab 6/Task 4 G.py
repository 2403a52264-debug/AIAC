### Using for Loop
def sum_to_n_for(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total
num = int(input("Enter a number: "))
print("Sum of first", num, "numbers (for loop):", sum_to_n_for(num))


### Using while Loop

def sum_to_n_while(n):
    total = 0
    i = 1
    while i <= n:
        total = total + i
        i = i + 1
    return total
num = int(input("Enter a number: "))
print("Sum of first", num, "numbers (while loop):", sum_to_n_while(num))
