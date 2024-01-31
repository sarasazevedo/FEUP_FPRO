'''A permutation of a string is any re-arrangement of its characters. For example: "bca" and "cba" are both permutations of "abc".

We can obtain all permutations of a string using the following recursive algorithm:

if the string is empty or has a single character then there is only one permutation (the string itself)
otherwise, the string has at least 2 characters:
recursively list all the permutations of the tail of string (i.e. without the first character)
for each of the results, consider all possibilities of inserting the first character of the original string into the result.
For example, to obtain the permutations of "abc" we first recursively compute the permutations of "bc". Assume that this subproblem is solved correctly, and we obtain ["bc", "cb"]. The permutations of the original string can be obtained by considering all insertions of 'a' into each of the strings "bc" and "cb", namely: ["abc", "bac", "bca", "acb", "cab", "cba"].

Write a recursive function permutations(str) that implements the algorithm above. The argument is a string, and the result should be a list of strings. The order of permutations in the result does not matter. You cannot use itertools.

Hint: you may find it useful to write an auxiliary function that returns the list of all insertions of a character into a string (this auxiliary function does not have to be recursive).'''
def permutations(string:str) -> list:
    if len(string) < 2: 
        return [string]

    result = []

    for i,j in enumerate(string):                           
        k = string[:i] + string[i+1:]              
        permut = permutations(k)   
        for permutation in permut:
            result.append(j+permutation)       

    return result

