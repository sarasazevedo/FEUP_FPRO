'''Write a Python function calc_triangular(n) that receives a positive integer n and calculates the nth triangular number. The nth triangular number (Tn) is the number of dots in the triangular arrangement with n dots on each side, and is equal to the sum of the n natural numbers from 1 to n (https://en.wikipedia.org/wiki/Triangular_number):

Tn=∑nk=1k=1+2+3+…+n 
print(calc_triangular(1))
1
print(calc_triangular(3))
6
print(calc_triangular(10))
55
print(calc_triangular(23))
276
'''

def calc_triangular(n):
    soma = 0
    for i in range(0, n+1):
        soma += i

    return soma 
