'''Write a Python function mult(M, N) that computes the matrix multiplication between the matrices of integers M and N, in that order. When the matrices’ dimensions are not compatible, the function must return an empty list.

You cannot use numpy.'''
def mult(M, N):
    rows = len(M)
    cols = len(N[0])
    res = []

    if len(M[0]) != len(N):
        return []
        
    for i in range(rows):
        res.append([0] * cols)

    for i in range(rows):
        for j in range(cols):
            for k in range(len(N)):
                res[i][j] += M[i][k] * N[k][j]

    return res

