'''Write a Python function longest_prefix(words) that, given a non-empty list of words called words, returns the longest common prefix to all the words.

For example: If words=["apple", "apply", "ape", "april"], then the biggest prefix is "ap".

You should use the divide and conquer strategy to find out the longest prefix, as it is depicted in the figure bellow:
1. if the list has one element, then the longest prefix is the element itself;
2. for a list with two elements or more: divide the list into two halves, recursively find each half's common prefix and determine the two results' common prefix.
'''

def longest_prefix(words):
        if not words: 
            return ""
        
        if len(words) == 1:
            return words[0]
        
        words.sort()
        prefix = ""
        
        for x, y in zip(words[0], words[-1]):
            if x == y: 
                prefix += x
            else: 
                break
        return prefix