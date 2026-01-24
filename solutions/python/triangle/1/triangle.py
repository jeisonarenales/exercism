def greather_than_zero(sides):
    if sides[0] > 0 and sides[1] > 0 and sides[2] > 0:
        return True
    else:
        return False

def sum_of_lengths(sides):
    a_b = sides[0] + sides[1]
    b_c = sides[1] + sides[2]
    a_c = sides[0] + sides[2]
    
    return a_b >= sides[2] and b_c >= sides[0] and a_c >= sides[1]

def equilateral(sides):
    return greather_than_zero(sides) and sum_of_lengths(sides) and sides[0] == sides[1] and sides[1] == sides[2]


def isosceles(sides):
    return greather_than_zero(sides) and sum_of_lengths(sides) and (sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2])


def scalene(sides):
    return greather_than_zero(sides) and sum_of_lengths(sides) and sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
