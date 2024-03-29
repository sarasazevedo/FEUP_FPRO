'''Recall the middle square algorithm for pseudo-random number generation: start with some integer number, square it and take the middle digits; then use that number as the seed for the next generation (see the wikipedia).

This algorithm is not a very good pseudo-random generator because it often ends in a cycle that just repeats the same numbers over and over again. For example: using 4 digits and starting with initial number 7492 we obtain:
7492-1300-6900-6100-2100-4100-8100
So after the first 3 iterations the cycle repeats the 4 numbers 6100, 2100, 4100, 8100.

Write a function cycle_length(number, digits) that computes the length of the cycle generated by a given starting number and for a given number of digits.

You may use the function to compute the next middle square given below:

def next_middle_square(number, digits):
   """Compute the next pseudo-random using the 
      middle square algorithm and the given number of digits."""
   k = digits // 2         # half of the number of digits
   square = number*number  # compute the square
   middle = (square // (10**k)) % (10**digits)   # extract middle part
   return middle
Hint: use a set to record the numbers that have already been generated and check for repetition.
'''
def cycle_length(number, digits):
    visited = {}
    while True:
        if number in visited:
            return len(visited) - visited[number]
        visited[number] = len(visited)
        number = next_middle_square(number, digits)

def next_middle_square(number, digits):
    k = digits // 2         # half of the number of digits
    square = number*number # compute the square
    middle = (square // (10**k)) % (10**digits)   # extract middle part
    return middle

