from Task_3 import is_sentence_palindrome

test_sentences = [
    # Test case 1
    "A man a plan a canal Panama",   
    # returns: True

    # Test case 2
    "No lemon, no melon",           
    # returns: True

    # Test case 3
    "Was it a car or a cat I saw?", 
    # returns: True

    # Test case 4
    "Never odd or even",            
    # returns: True

    # Test case 5
    "Hello World",                  
    # returns: False

    # Test case 6
    "Palindrome",                   
    # returns: False

    # Test case 7
    "Step on no pets",             
    # returns: True

    # Test case 8
    "Eva, can I see bees in a cave?",
    # returns: True

    # Test case 9
    "12321",                         
    # returns: True

    # Test case 10
    "12345",                         
    # returns: False

    # Test case 11
    "",                              
    # returns: True (empty string is trivially palindrome)

    # Test case 12
    " ",                             
    # returns: True (only space, still palindrome)

    # Test case 13
    "Able was I, ere I saw Elba",    
    # returns: True

    # Test case 14
    "Madam In Eden, I’m Adam",       
    # returns: True

    # Test case 15
    "Yo, Banana Boy!",               
    # returns: True
]

if __name__ == "__main__":
    for i, sentence in enumerate(test_sentences, start=1):
        print(f"Test case {i} \n Sentence: {sentence!r} -> {is_sentence_palindrome(sentence)}")
