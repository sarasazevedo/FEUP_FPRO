'''Given a tuple of size > 3, write a Python function triplet(tup) that finds a triplet (a, b, c) where a, b, c are elements of tup, such that their sum is zero (a + b + c = 0).

In case there is more than one triplet that sums up to zero, return the first occurrence when searching by lexicographical order of indexes. In case there are none, return an empty tuple, ().'''

def triplet(tup): 
    for i in range(len(tup)):
        for j in range(i+1, len(tup)):
            for k in range(j+1, len(tup)):
                if tup[i] + tup[j] + tup[k] == 0:
                    x = tup[i]
                    y = tup[j]
                    z = tup[k]
                    return (x,y,z)
    return ()
