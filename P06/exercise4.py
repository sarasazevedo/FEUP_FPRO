'''A magic square is a matrix of n*n integer numbers such that every line, column and two diagonals sum the same value.

Define a function magic(mat) that tests if a matrix mat (represented by a list of lists of integers) is a magic square. The matrix can have any square dimensions n*n such that n>=3. The result returned by the function should be a Boolean value: True if the matrix is a magic square and False otherwise.

Note: Your code must pass all tests (all-or-nothing) to get a grade.'''
def magic(mat):
    n = len(mat)
    d1 = 0
    d2 = 0

    for i in range(n):
        d1 += mat[i][i]
        d2 += mat[i][len(mat)-i-1]

    for i in range(n):
        soma=0
        for j in range(n):
            soma=soma+mat[i][j]
    
    for j in range(n):
        soma1=0
        for i in range(n):
            soma1=soma1+mat[i][j]
    
    if(d1==d2) and (soma==d1) and (soma==d2) and (soma1==d1) and (soma1==d2):
        return True
    else:
        return False
    