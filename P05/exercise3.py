'''Write a Python function mask_data(data, n_characters, position) that receives a string data and returns the masked string in which the first or last n_characters characters are masked as an asterisk, according to position.

The position admits two values: 'begin' — indicating that masking must consider the first n_characters characters of the original string — and 'end' — indicating that masking must consider the last n_characters of the original string.

If n_characters is zero then the function must return the original string. If n_characters is greater than the total of characters of the string or less than zero then the function must return all the characters masked by asterisks.'''
import string

def mask_data(data, n_characters, position):
    result = ""
    if(n_characters == 0):
        return data
    
    if(position == "begin"):
        for i in range(0,n_characters+1):
            result = n_characters * "*" + data[n_characters:]
    else: 
         for i in range(0,len(data)-n_characters): 
             result = data[0:len(data)-n_characters] + n_characters * "*"
            
    return result 
