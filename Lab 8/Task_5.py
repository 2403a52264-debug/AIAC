def convert_date_format(date_str):
    try:
        year, month, day = date_str.split("-")
        return f"{day}-{month}-{year}"
    except Exception:
        return "Invalid format"


if __name__ == "__main__":
    # Test case 1
    input_date = "2023-10-15"
    print(f'"{input_date}" → "{convert_date_format(input_date)}"')
    # returns: "2023-10-15" → "15-10-2023"

    # Test case 2
    input_date = "1999-01-01"
    print(f'"{input_date}" → "{convert_date_format(input_date)}"')
    # returns: "1999-01-01" → "01-01-1999"

    # Test case 3
    input_date = "15/10/2023"
    print(f'"{input_date}" → "{convert_date_format(input_date)}"')
    # returns: "15/10/2023" → "Invalid format"
