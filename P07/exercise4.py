'''Write a Python function isomorphic(astring1, astring2) that given two strings of the same length, determines if they are isomorphic.  Two strings are called isomorphic if the characters of each of the strings can be remapped to get the other string.

Remapping a character means replacing all occurrences of it with another character, while preserving the ordering of the characters. No two characters may map to the same character, but a character may map to itself. For example, the strings "foo" and "app" are isomorphic because it is possible to map 'f' to 'a' and 'o' to 'p'.  The strings "bar" and "foo" are not isomorphic because it is not possible to map both 'a' and 'r' to 'o'. Notice that this must be possible in both directions

The function must return a properly formatted string:

'<astring1> and '<astring2>' are isomorphic, if the strings are isomorphic

or

'<astring1>' and '<astring2>' are not isomorphic, otherwise

Hint: Make an auxiliary function to compute one unidirectional mapping.'''
def isomorphic(astring1, astring2):
    dict = {}
    valueslist = []
    result = ()
    
    for i, values in enumerate(astring1):
        dict[values] = astring2[i]
    
    for i in dict.values():
        if i not in valueslist:
            valueslist.append(i)
            continue
        else:
            return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
    
    for i in astring2:
        if i not in dict.values():
            return "'{}' and '{}' are not isomorphic".format(astring1, astring2)
            
    for key, value in dict.items():
        result += ((key, value),)
    
    return "'{}' and '{}' are isomorphic".format(astring1, astring2, str(list(result)))
