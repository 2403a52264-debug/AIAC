with open("example.txt", "w") as f:
    f.write("Hello,world!")

with open("data1.txt", "w") as f1:
    f1.write("First file content\n")

with open("data2.txt", "w") as f2:
    f2.write("Second file content\n")

print("Files written successfully")

try:
    with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
        for line in infile:
            outfile.write(line.upper())
    print("Processing done")
except FileNotFoundError:
    print("input.txt not found.")

try:
    with open("numbers.txt", "r") as numfile:
        nums = numfile.readlines()
    squares = []
    for n in nums:
        n = n.strip()
        if n.isdigit():
            squares.append(int(n) * int(n))
    with open("squares.txt", "w") as sqfile:
        for sq in squares:
            sqfile.write(str(sq) + "\n")
    print("Squares written")
except FileNotFoundError:
    print("numbers.txt not found.")