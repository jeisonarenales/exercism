def leap_year(year):
    is_leap_year = False
    # divisible by 4 
    if year % 4 == 0:
        is_leap_year = True
    # skip it if it's a new century
    if year % 100 == 0:
        is_leap_year = False
        # unless the century is divisible by 400
        if year % 400 == 0:
            is_leap_year = True
    return is_leap_year
