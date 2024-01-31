'''Binary trees can be used to make it fast to search for ordered information. Each parent node can have two children nodes (left and right) in this data structure, which are also binary trees.
A binary tree is one of:

1. None, representing an empty tree;
2. a tuple of the form (key, value, left, right), where left and right are binary trees; the left tree keys are smaller than the parent's key, while the right tree keys are bigger than the parent's key.

Write a function search_tree(key, tree) that, given a string as key and the first node as tree, returns a pair (value, visited) or None if the key does not occur in the tree; the value is in the same tuple as key and visited is the list of keys that were visited in the search.

Hint: Take advantage of the binary structure of the tree to visit as few keys as possible.
'''
def search_tree(target_key, current_tree, visited=[]):
    if current_tree == None:
        return None
    
    key, value, left, right = current_tree
    visited = visited + [key]
    
    if key == target_key:
        return (value, visited)
    if key > target_key:
        return search_tree(target_key, left, visited)
    if key < target_key:
        return search_tree(target_key, right, visited)