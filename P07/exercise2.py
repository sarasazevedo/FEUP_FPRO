'''Write a Python function roman_to_integer(astring) that, given a Roman numeral in the standard form (as a string), returns its corresponding decimal value (as an integer). Use the following dictionary to map each individual Roman symbols to its decimal value:

        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }'''
roman_to_decimal = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
    }

def roman_to_integer(a_string):
    res = 0
    comp = len(a_string)
    for i, c in enumerate(a_string):
        if i<comp-1 and roman_to_decimal[c] < roman_to_decimal[a_string[i+1]]:
            res -= roman_to_decimal[c]
        else:
            res += roman_to_decimal[c]
    
    return res
            
