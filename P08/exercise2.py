'''The greatest common divisor (GCD) of a
 and b
 is the largest integer that evenly divides both numbers (with no remainder). We can compute the GCD of two non-negative numbers a
, b
 by the following iterative algorithm (known as Euclid's algorithm):

def gcd(a, b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a
Write a tail recursive Python function gcd_rec(a, b) that implements the same algorithm. You cannot use loops or the math library.'''

def gcd_rec(n1,n2):
    if n2 == 0:
        return n1
    else:
        return gcd_rec(n2,n1%n2)