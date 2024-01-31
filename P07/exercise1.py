'''Write a Python function switch_dict(adict) that receives a dictionary adict and returns a new dictionary having adict values as the keys and lists of adict keys as values. In case of duplicate values in adict, the corresponding keys should be added to the list of values in the same order as they occur in the original dictionary.

For example, given the dictionary {'jan': 'winter', 'feb': 'winter', 'may': 'spring', 'july': 'summer', 'august':'summer'}, the function should return {'winter': ['jan', 'feb'], 'spring': ['may'], 'summer': ['july', 'august']}.'''

def switch_dict(adict):
    result = {}
    for key, value in adict.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)
    return result
