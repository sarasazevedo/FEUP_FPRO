"""Write a Python program that asks the user to input a positive 4-digit number n and prints the numbers that compose its expanded form.

For example, the expanded form of 1543 is 1000+500+40+3. The expected output for a user input of 1543 is

1000
500
40
3
"""
number = int(input())
print((number//1000) * 1000)
number = number % 1000
print((number // 100) * 100)
number = number % 100
print((number // 10) * 10)
print(number%10)