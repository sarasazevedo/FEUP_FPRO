''''Given a list of numbers 𝑥=[𝑥1,𝑥2,𝑥3,…𝑥𝑛], the forward differences of 𝑥 are [𝑥2−𝑥1,𝑥3−𝑥2,...,𝑥𝑛−𝑥𝑛−1]
Write a function differences(alist) that computes the forward differences of a list. Assume that the list has at least one element. You cannot use loops.
Hint: use zip to combine the list with its own tail (i.e. the list without its first element) and map to compute the differences.'''

def differences(alist):
    return list(map(lambda x: x[1] - x[0], zip(alist, alist[1:])))
