import time
start_time = time.time()

# Fixed: Direct list comprehension without intermediate list
# This eliminates the memory bug by not creating the unnecessary 'nums' list
squares = [n**2 for n in range(1, 1000000)] # List of squares of numbers

print(len(squares)) # Length of the list of squares

end_time = time.time()
print(end_time - start_time) # Time taken by the program