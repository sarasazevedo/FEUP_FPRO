'''Recall from exercise 3 of QP04 that the variance of a list of samples 𝑥=[𝑥1,𝑥2,…,𝑥𝑁] can be computed by the formula
𝜎(𝐱)=∑𝑁𝑖=1(𝑥𝑖−𝐱¯)2𝑁
where 𝑥¯ is the average of the values of 𝑥, i.e. 𝑥¯=1𝑁∑𝑁𝑖=1𝑥𝑖
Write a function variance(alist) that computes and returns the variance of a list of numbers. You should round the result to 3 decimal places. You cannot use loops.
Hint: use sum and map.'''

def variance(alist):
    n = len(alist)
    mean = sum(alist) / n
    squared_diff = map(lambda x: (x - mean)**2, alist)
    result = sum(squared_diff) / n
    return round(result, 3)