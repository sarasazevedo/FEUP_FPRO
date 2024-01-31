'''Write a Python function var_numbers(number, precision) that returns the variance of all positive integers up to and including number. The second parameter defines the precision of the result and has the default value of 2. Use round to approximate the result to the given precision.

Remember the formula of variance:

σ(x)=∑Ni=1(xi−x¯)2N

where xi
 is the i-th element of the sequence 1,2,...,number
, and x¯
 is the average of all those values.

Hint: It is easier if you write an additional function sum_numbers(number) that returns the sum of all positive integers up to and including number and then use this function in the var_numbers function.
print(var_numbers(3))
0.67
print(var_numbers(10, 1))
8.2
print(var_numbers(15, 3))
18.667
print(var_numbers(7))
4.0
'''

def sum_numbers(num):
    res = 0
    for i in range(1, num + 1):
        res += i
    return res

def var_numbers(num, precision = 2):
    res = 0
    res2 = sum_numbers(num) / num
    for i in range(1, num + 1):
        temp = (i - res2)**2
        res += temp
    res = res / num

    return round(res, precision)
