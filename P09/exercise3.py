'''Write a function x_union(list1, list2) that returns the exclusive union of two lists of pairs. The exclusive union contains the pairs whose first component occurs in one of the two lists but not on both lists. 
For example:
>>> x_union([('a', 1), ('b', 2)], [('c', 3), ('a', 0)])
[('b', 2), ('c', 3)]
The pairs of the first list should occur before those in the second list and in the same order as the two original lists. You cannot use loops.
Hint: use map to project the first component and filter to eliminate values from each list.'''

def x_union(list1, list2):
    proj_list1 = list(map(lambda x: x[0], list1))
    proj_list2 = list(map(lambda x: x[0], list2))

    unique_list1 = filter(lambda x: x[0] not in proj_list2, list1)
    unique_list2 = filter(lambda x: x[0] not in proj_list1, list2)

    return list(unique_list1) + list(unique_list2)

