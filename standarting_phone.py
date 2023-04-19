def unify_phone(phone: str) -> str:
    """Will bring given phone to a standart look"""
    
    data = phone.replace(" ", "")

    number = []
    for num in data:
        if num.isdigit():
            number.append(num)
    
    if len(number) == 11:
        number[0] = "8"
        number.insert(1, " (")
        number.insert(5, ") ")
        number.insert(9, "-")
        number.insert(12, "-")

    if len(number) == 10 and int(number[0]) == 9:
        number.insert(0, "8")
        number.insert(1, " (")
        number.insert(5, ") ")
        number.insert(9, "-")
        number.insert(12, "-")

    final_number = "".join(number)
    return final_number


