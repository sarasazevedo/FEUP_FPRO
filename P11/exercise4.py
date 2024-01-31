'''Consider a convex function f: ℝ → ℝ which maps a number into another number and is defined in the interval [0, 1]; for example: (see image)
In this case, the root (zero) of a numeric function in the interval 0 to 1 can be found using the Bisection method (a type of binary search), as follows:
1. Define the lower and upper bound variables as 0 and 1, respectively;
2. Evaluate the function at the midpoint between the lower and upper bound;
3. If f(lower) and f(midpoint) have the same sign, then lower := midpoint;
4. Otherwise, upper := midpoint;
5. Go back to 2 until 𝑛 rounds have been performed;
6. Return midpoint rounded to 5 digits
Write a Python function called bisect(f, n) that, given a function f and the number of rounds n, returns the root approximation at the 𝑛𝑡ℎ round.
'''
def bisect(f, n):
    lower = 0
    upper = 1

    for _ in range(n):
        midPoint = (upper + lower) / 2
        if f(lower) * f(midPoint) > 0:
            lower = midPoint
        else:
            upper = midPoint
    return round(midPoint, 5)