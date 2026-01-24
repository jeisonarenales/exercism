def steps(number):
    if number < 1:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
    result = number
    iterations = 0
    while result != 1:
        iterations += 1
        if result % 2 == 0:
            result = result / 2
        else:
            result = result * 3 + 1 
    return iterations