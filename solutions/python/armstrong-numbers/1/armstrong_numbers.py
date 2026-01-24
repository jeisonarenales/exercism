def is_armstrong_number(number):
    int_str = str(abs(number))
    digits = len(int_str)
    a_number = 0
    for i in int_str:
        a_number += int(i) ** digits
    return a_number == number
    
        