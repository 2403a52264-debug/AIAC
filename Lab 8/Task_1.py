import re

def is_valid_email(email: str) -> bool:
    # Must contain exactly one '@'
    if email.count('@') != 1:
        return False
    
    # Must contain at least one '.' after '@'
    if '.' not in email.split('@')[1]:
        return False
    
    # Must not start or end with special characters
    if email[0] in ".@_-":
        return False
    if email[-1] in ".@_-":
        return False
    
    # Regex for allowed characters
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    if not re.match(pattern, email):
        return False
    
    return True



if __name__ == "__main__":
    #Test case 1
    print("siddu@example.com ->", is_valid_email("siddu@example.com")) 
    #  return: True
    #Test case 2
    print("siddu@@mail.com ->", is_valid_email("siddu@@mail.com"))    
    #  return: False
