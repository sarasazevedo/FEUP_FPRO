'''Write a Python function find_me(f, limits) that, given a function f and a tuple limits with two integers representing the search limits, returns how many iterations are necessary until the desired number is found.

The function f receives a number and returns either -1 (smaller) or +1 (bigger) or 0 (found). For example, f=lambda n: -1 if n > 30 else 1 if n < 30 else 0. That is, if we are searching for the number 30, then f(20) returns 1 (because 20 < 30), f(30) returns 0 (since 30 is the correct number!), and f(60) returns -1 (because 60 > 30).

You must start by guessing the middle number (that counts as an iteration) and use binary search [wikipedia] to adjust the limits until the solution is found.
'''

def find_me(f,limits):
    
    while True:
     mid = (limits[0] + limits[1]) // 2
     probe = f(mid)
     if probe == 0:
        return 1
     if probe == -1:
        return 1 + find_me(f,(limits[0],mid - 1))
     if probe == 1: 
        return 1 + find_me(f,(mid + 1,limits[1]))