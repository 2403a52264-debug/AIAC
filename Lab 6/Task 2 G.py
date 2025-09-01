### Using for Loop
def print_multiples_for():
    number = int(input("Enter a number:"))
    print("First 10 multiples of",number,"using for loop:")
    for i in range(1,11):
        print(number,"x",i,"=",number*i)
print_multiples_for()

### Using while Loop
def print_multiples_while():
    number = int(input("Enter a number:"))
    print("First 10 multiples of",number,"using while loop:")
    i=1
    while i <= 10:
        print(number,"x",i,"=",number*i)
        i = i+1
print_multiples_while()