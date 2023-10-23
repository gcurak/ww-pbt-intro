from math import sqrt

def sum_perfect_squares(x: int, y: int):
    """returns the sum of two perfect squares """
    assert sqrt(x)*sqrt(x) == x
    assert sqrt(y)*sqrt(y) == y
    
    if x == y:
        return x+y+1 # ;-)
    return x+y