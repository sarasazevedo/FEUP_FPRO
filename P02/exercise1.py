"""Write a Python program that asks the user to input a digit n (0-9), calculates the expression n + nn + nnn and prints its value.
For example: for a user input 5, the output must be 615 (5 + 55 + 555)."""

num1 = int(input())
res = num1 + (num1*11) + (num1*111)
print(res)
