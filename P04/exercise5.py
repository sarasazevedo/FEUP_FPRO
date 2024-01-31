'''Write a Python function deriv(f) that receives a function f and returns a new function that computes df(x)
 numerically using the approximation below. Use round to approximate the result to 3 decimal places.

Recall that the derivative df(x)
 of a real function f(x)
 is defined as a limit:

df(x)=limh→0f(x+h)−f(x)h

For a small h, we can numerically compute the derivative using the equation:

df(x)=f(x+h)−f(x)h,

For the sake of simplicity, consider h=0.001
.

Por exemplo:

Teste	Resultado
def f(x): 
    return x*x + 2*x + 2
print(deriv(f)(3))
8.001
import math
def g(x):
    return math.sin(x) / x
print(deriv(g)(3.14))
-0.319
import math
def f(x):
    return math.log(x+10)
print(deriv(f)(-5))
0.2
def f(x):
    return 3/x + 5
print(deriv(f)(55.231))
-0.001
'''
def deriv(f):
    h = 0.001
    def df(x):
        return round((f(x+h)-f(x))/h,3)
    return df 
