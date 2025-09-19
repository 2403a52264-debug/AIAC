from Task_5 import convert_date_format

test_dates = [
    # Test case 1
    "2023-10-15",  
    # returns: "15-10-2023"
    
    # Test case 2
    "1999-01-01",  
    # returns: "01-01-1999"
    
    # Test case 3
    "2000-12-31",  
    # returns: "31-12-2000"
    
    # Test case 4
    "2024-02-29",  
    # returns: "29-02-2024"
    
    # Test case 5
    "15/10/2023",   
    # returns: "Invalid format"
    
    # Test case 6
    "2023.10.15",   
    # returns: "Invalid format"
    
    # Test case 7
    "20231015",     
    # returns: "Invalid format"
    
    # Test case 8
    "2023-13-01",  
    # returns: "01-13-2023"
    
    # Test case 9
    "abcd-ef-gh",   
    # returns: "gh-ef-abcd"
    
    # Test case 10
    "",            
    # returns: "Invalid format"
]

if __name__ == "__main__":
    for i, date_str in enumerate(test_dates, start=1):
        print(f'"{date_str}" → "{convert_date_format(date_str)}"')
