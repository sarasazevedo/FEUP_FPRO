'''Write a Python program that takes an integer num, provided by the user, and outputs the multiplication table with lines: num x index = res, where res = num * index and index is a number that goes from 1 to a maximum of 10.

When the number is multiplied by itself, the displayed format should be num ^ 2 = res and the table is finished immediately.

For example for num = 5 the output is:

5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 ^ 2 = 25 
'''

num = int(input())

for i in range(1, 11):
    if (i == num):
        print(str(num) + " ^ 2 = " + str(num * num))
        break
    else:
         print(str(num) + " x " + str(i) + " = " + str(num * i))

