def square(number):
    if number > 64 or number < 1:
        # when the square value is not in the acceptable range        
        raise ValueError("square must be between 1 and 64")
    else:
        if number == 1 or number == 2:
            return number
        grains = 2
        for i in range(3,number + 1):
            grains += grains
        return grains


def total():
    grains = 1
    total = 0
    for i in range(64):
        total += grains
        grains = grains + grains
    return total
        
