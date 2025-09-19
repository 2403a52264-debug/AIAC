from Task_2 import assign_grade

test_scores = [
    # test case 1
    100,   
    # returns: A
    
    # test case 2
    95,    
    # returns: A
    
    # test case 3
    90,    
    # returns: A
    
    # test case 4
    89,    
    # returns: B
    
    # test case 5
    85,  
    # returns: B
    
    # test case 6
    80,  
    # returns: B
    
    # test case 7
    79,  
    # returns: C
    
    # test case 8
    72,  
    # returns: C
    
    # test case 9
    70,  
    # returns: C
    
    # test case 10
    69,  
    # returns: D
    
    # test case 11
    65,  
    # returns: D
    
    # test case 12
    60,  
    # returns: D
    
    # test case 13
    59,  
    # returns: F
    
    # test case 14
    30,  
    # returns: F
    
    # test case 15
    0,   
    # returns: F
    
    # test case 16
    -5,   
    # returns: Invalid
    
    # test case 17
    105,   
    # returns: Invalid
    
    # test case 18
    75.5   
    # returns: C (floats allowed)
]

if __name__ == "__main__":
    for idx, score in enumerate(test_scores, start=1):
        print(f"Test Case {idx}: \n Score={score} -> {assign_grade(score)}")
