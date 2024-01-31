'''A possible representation of a multi-graph is as a tuple of pairs, each representing a single edge. For example, the multi-graph of the figure would be represented as (('A','B'), ('A','C'), ('B','C'), ('C','B'), ('A','B')).

A more succinct representation would be as a tuple of triples, each representing a multi-edge associated with a multiplicity. The same graph would then be represented as (('A',2,'B'), ('A',1,'C'), ('B',1,'C'), ('C',1,'B')).

Write a Python function multi(g) that given a multi-graph g as a tuple of pairs, returns its representation as a tuple of triples with multiplicities. The order of triples in the tuple is irrelevant.'''

def multi(g):
    multi = {}
    for i in g:
        if i in multi:
            multi[i] += 1
        else:
            multi[i] = 1

    triples = [(i[0], multi[i], i[1]) for i in multi]

    return tuple(triples)


