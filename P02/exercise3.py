'''Convert the following diagram to computer code in Python.

The operations should be done sequentially. Be aware of the precedence of the operations and that operands higher up in the diagram have precedence over operands lower down. (See figure)'''

number1 = int(input())
number2 = int(input())
number3 = int(input())
res1 = (number1 * 3) - 5
res2 = (number2 + 6) // 4
res3 = number3 ** 2 
print(res1 + res2)
print(res2 - res3)
