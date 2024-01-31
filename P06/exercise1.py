'''Write a Python function local_minima(alist) that receives a list alist and returns a list with all local minima for each neighbourhood of three elements.

For example, if alist=[4, 2, 2, 5, 1], then we have 3 neighbourhoods: (i) [4, 2, 2]; (ii) [2, 2, 5]; (iii) [2, 5, 1]. In this case, there is only one local minima: [1].

Notice that 2 is never a local minimum because it has another value equal to it in the neighbourhood.'''
def local_minima(alist):
    result=[]
    for i in range(1,len(alist)-1):
        window = alist[i-1:i+2]
        if window.count(min(window))==1:
            result.append(min(window))
        
    return result
