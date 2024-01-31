'''Use a list comprehension inside a function square_odds(values) that, given a string values with a comma-separated list of numbers, 
returns a string with comma-separated squares of each odd number in a list.'''

def square_odds(values):
    vals = values.split(',')
    square = [int(x)**2 for x in vals]
    odds = [str(x) for x in square if not x%2==0]
    return ','.join(odds)
