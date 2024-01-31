'''A sparse vector is a vector whose entries are almost all zero, e.g., [0, 1, 0, 0, 0, 0, 0, 0, 2, 0]. For memory efficiency, sparse vectors can be represented as dictionaries with keys representing the indices of non-zero values, and then the value of a key corresponds to the value of the vector at that index. For example, the vector above can be stored as the dictionary {1: 1, 8: 2}.

Write a Python function sparse_dot_product(dict1, dict2) that computes the inner product of two sparse vectors, dict1 and dict2, represented as dictionaries.

The inner product of two vectors is given as: a⋅b=∑ni=1aibi=a1b1+a2b2+...+anbn'''
def sparse_dot_product(dict1, dict2):
    result = 0
    for k,v in dict1.items():
        if k in dict2: 
            result += v * dict2[k]
    return result
    