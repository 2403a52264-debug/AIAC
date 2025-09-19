from Task_1 import is_valid_email

emails = [
    #Test case 1
    "john.doe123@mail.co",
    #return: True
    
    #Test case 2                                
    "name_surname@domain.org",
    #return: True
    
    #Test case 3        
    "abc.def@sub.domain.com", 
    #return: True
    
    #Test case 4  
    "user123@site.in",
    #return: True
    
    #Test case 5
    "@example.com",
    #return: False
    
    #Test case 6        
    "user@",
    #return: False
    #Test case 7
    ".username@mail.com",   
    #return: False
    #Test case 8
    "username@mail.com.",
    #return: False
    #Test case 9
    "user#mail.com",
    #return: False
    #Test case 10
    "username@domaincom",
    #return: False
    #Test case 11
    "username@.com",
    #return: False
    #Test case 12  
    "username@domain..com",
    #return: False
    #Test case 13
    "user name@mail.com"
    #return: False
]

if __name__ == "__main__":
    for email in emails:
        print(f"{email:30} -> {is_valid_email(email)}")
