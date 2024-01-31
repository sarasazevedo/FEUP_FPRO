'''We can sort a list of numbers in ascending order by using the following recursive merge sort algorithm.

To sort a list of length n > 1:
1. divide the list into two smaller lists of (approximately) half the length;
2. recursively sort each of two halves;
3. merge the two sorted results into a single list using the function merge(xs, ys) (see bellow).
When we reach lists of length 0 or 1 we can stop (because they are trivially already sorted).

Use the merge(xs, ys) function, which implements the Merge algorithm [wikipedia], available at [Github].

Write a function msort(xs) that sorts a list xs of integers using this method. You cannot use the built-in function sorted or the list method sort.'''

def merge(xs, ys):
    """ Merge sorted lists xs and ys. Return a sorted result. """
    result = []
    xi = 0   # i-th element of xs
    yi = 0   # i-th element of ys

    while True:
        if xi >= len(xs):           # If xs list is finished,
            result.extend(ys[yi:])  # Add remaining items from ys
            return result           # And we're done.

        if yi >= len(ys):           # Same again, but swap roles
            result.extend(xs[xi:])
            return result

        # Both lists still have items, copy smaller item to result.
        if xs[xi] <= ys[yi]:
            result.append(xs[xi])
            xi += 1
        else:
            result.append(ys[yi])
            yi += 1

def msort(xs):
    
    if len(xs) <= 1:
        return xs
    
    midPoint = len(xs) // 2
    lx = msort(xs[:midPoint])
    rx = msort(xs[midPoint:])

    
    return merge(lx,rx)
