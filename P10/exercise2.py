'''Write a Python function comprehensions(i, j) that, given two integers i and j, returns a tuple with three components computed in the interval [i, j]:
1. A list with all numbers in that interval that end in 3 or 8.
2. A tuple with the square root, rounded to 2 decimals, of numbers in that interval.
3. A dictionary where the key is a number and the value is the corresponding character from the ASCII table, of numbers in that interval.
You cannot use loops, only comprehensions or map and filter.'''

import math

def comprehensions(i, j):
    lista = [x for x in range(i, j+1) if x % 10 == 3 or x % 10 == 8]
    sqrts = tuple([round(math.sqrt(x), 2) for x in range(i, j+1)])
    asci = {x:chr(x) for x in range(i,j+1)}
    return (lista, sqrts, asci)

