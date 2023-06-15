def equilateral(sides):
    if not is_triangle(sides):
        return False
        
    return len(set(sides)) == 1


def isosceles(sides):
    if not is_triangle(sides):
        return False

    return len(set(sides)) <= 2


def scalene(sides):
    if not is_triangle(sides):
        return False
        
    return len(set(sides)) == 3

def is_triangle(sides):
    a, b, c = sorted(sides)
    if sum(sides) == 0:
        return False
        
    if ( ((a + b) >= c) and
         ((b + c) >= a) and
         ((a + c) >= b) ):
        return True
    else:
        return False

print(isosceles([4,4,4]))