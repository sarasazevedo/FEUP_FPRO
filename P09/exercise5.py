'''The bounding box of a list of 2 dimensional points is the smallest rectangle that encloses all the points.
Write a function bounding_box(pts) that computes the bounding box of a list of points given as (𝑥,𝑦)
 tuples. You may assume that the list is not empty. The result should be a tuple of (𝑥𝑚𝑖𝑛,𝑦𝑚𝑖𝑛,𝑥𝑚𝑎𝑥,𝑦𝑚𝑎𝑥).
You cannot use loops or the built-in min and max functions.
Hint: use map to project the 𝑥 or 𝑦 coordinates and functools.reduce to compute the maximum and minimum of a sequence.'''

def bounding_box(pts:list) -> tuple:
    x = list(map(lambda x: x[0], pts))
    y = list(map(lambda y: y[1], pts))
    from functools import reduce as r
    return (r(lambda i,j: i if i<j else j, x), 
            r(lambda i,j: i if i<j else j, y),
            r(lambda i,j: i if i>j else j, x),
            r(lambda i,j: i if i>j else j, y))