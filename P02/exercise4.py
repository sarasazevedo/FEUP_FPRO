"""Consider the sentence: "I ate half of the cheesecake my two roommates made.".

Write a Python program that stores the sentence in chunks in different variables, as follows: first variable - “I ate”, second variable - “half”, third variable - “of the cheesecake my”, fourth variable - “two”, fifth variable - “roommates made.”; and prints the sentence using the concatenation of those variables.
Now, reassign the second variable with float value 0.5 and the fourth variable with integer value 2. You will get an error message if you try to rerun the program. After you read the error message carefully, fix the problem without using the string literal "0.5" or "2"."""

first = "I ate"
second = 0.5
third = "of the cheesecake my"
fourth = 2
fifth = "roommates made."
print(first + " " + str(second) + " " + third + " " + str(fourth) + " " + fifth)