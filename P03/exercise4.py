''' 
Write a Python script that prints a square filled with the # character for a given dimension, greater or equal to 3.

The square centre must be filled with either one or four zeros (0), depending on whether the dimension is odd or even.

For example for dimension 4 the, output is:

####
#00#
#00#
####
and for dimension 5, the output is:

#####
#####
##0##
#####
#####'''

num = int(input())
div = num//2

if (num%2 != 0):
    for i in range(0, num):
        for j in range(0, num):
            if (j == div) and (i == div):
                print("0", end = "")
                
            else:
                print("#", end = "")
                
        print(end = '\n')
                
else:
    for i in range(0, num):
        for j in range(0, num):
            if ((j == div) or j == div-1) and ((i == div) or (i == div-1)):
                print("0", end = "")
                
            else:
                print("#", end = "")
                
        print(end = '\n')