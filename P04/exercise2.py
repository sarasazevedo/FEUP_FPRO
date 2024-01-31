'''
Write a Python function adigits(a, b, c) that receives three integers, each one with a single decimal digit and returns the lowest integer number that can be assembled with the three digits given as parameters.
'''
def adigits(a, b, c):
    if a <= b and a <= c:
        a = a * 100
        if b <= c:
            b = b * 10
        else:
            c = c * 10
    elif b <= a and b <= c:
        b = b * 100
        if a <= c:
            a = a * 10
        else:
            c = c * 10
    else:
        c = c * 100
        if a <= b:
            a = a * 10
        else:
            b = b * 10

    return a + b + c
