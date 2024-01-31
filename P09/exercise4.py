'''An integer can be represented by a list of its digits. For example, 2345 can be represented by the list [2,3,4,5].
Define a function dec2int(alist) that, given a list of integers that represent the decimal digits of a number, computes that number. You may assume that the list is not empty.
You cannot use loops.
Hint: use functools.reduce with a function that adds a single digit to the result.
'''

from functools import reduce

def dec2int(alist):
    return reduce(lambda x, y: x * 10 + y, alist)