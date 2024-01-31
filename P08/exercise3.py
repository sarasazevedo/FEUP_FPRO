'''Write a recursive Python function max_path(tree) that given a tree, computes the value of the path that produces the highest value by summing the values of each node, starting from the root and ending in a leaf (a node without descendants).

A tree is either:

a single integer;
a triple (left, value, right) where value is an integer value of the node and left and right are the two trees.
For example, considering the tree ((2, 1, ((1, 2, 2), 2, 1)), 0, (5, 4, 2)) the function should return 9.

'''
def max_path(tree:tuple) -> int:
    if type(tree) == int: 
        return tree
    
    l = tree[1] + max_path(tree[0])
    r = tree[1] + max_path(tree[2])

    return max(l, r)