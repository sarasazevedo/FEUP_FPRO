'''Suppose we have two dictionaries with some keys that are common and (possibly) some that are distinct. We want to combine the two dictionaries into a single one. When a key belongs to only one of the dictionaries, then its value is kept. If the key occurs in both dictionaries, then the value in the combined dictionary should be given by applying some given function.
For example: if the dictionaries are {'a':1, 'b':2} and {'a':3, 'c':4} and the combination function is lambda x,y: x+y, then the result should be {'a':4, 'b':2, 'c':4}. The value for 'a' is 4=1+3 because it occurs in both dictionaries; the other keys occur in only one of the dictionaries, so their values are kept.
Write a pure function union_with(combine, dict1, dict2) that returns a new combined dictionary. The first argument is the combination function (which always takes two values to combine). Your function should not modify the original dictionaries, but instead construct a new dictionary. The order of construction of the dictionary does not matter.
Hint: use dictionary comprehensions.'''

def union_with(combine, dict1:dict, dict2:dict):
    keys = dict1.keys() | dict2.keys()
    result = {key: combine(dict1.get(key), dict2.get(key)) if key in dict1 and key in dict2 else dict1.get(key, dict2.get(key)) for key in keys}
    return result

