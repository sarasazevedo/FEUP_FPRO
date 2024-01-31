'''Binary relations are sets of pairs, and are useful to reason about many useful concepts, such as graphs. For instance, the transitive closure of a binary relation allows us to reason about reachability in a graph.

The transitive closure of a binary relation 𝑅 is defined as the union of successive compositions, i.e.:
⋃𝑖∈ℕ𝑅𝑖=𝑅∪𝑅∘𝑅∪𝑅∘𝑅∘𝑅∪…
If relation 𝑅 is finite, this process will necessarily end when the next step adds nothing to the union of the previous steps, that is:
𝑅𝑖+1⊆⋃𝑖𝑗=1𝑅𝑗
Recall also that the composition of two relations can be defined by comprehension as follows:
𝑅∘𝑆={(𝑎,𝑏)|∃𝑐⋅(𝑎,𝑐)∈𝑅∧(𝑐,𝑏)∈𝑆}
For instance, if you have a binary relation 𝑅 defined as {(1,2), (2,3), (3,4)}, 𝑅∘𝑅 will add pairs (1,3) and (2,4), and then 𝑅∘𝑅∘𝑅 will just add pair (1,4). The next step 𝑅∘𝑅∘𝑅∘𝑅 adds no new pair, so the process stops and the final result is {(1,2), (1,3), (1,4), (2,3), (2,4), (3,4)}.
Write a pure function transitive_closure(r) that receives a binary relation r as input, represented as a set of pairs, and returns its transitive closure. Your function should not modify the original relation, but instead construct a new set.
Hint: Define the composition of relations in an auxiliary function, and recall Python supports sets by comprehension.'''

def transitive_closure(r:set):
    def rec(r): 
        newr = {(x[0],y[1]) for x in r for y in r if x[1] == y[0]}
        if not newr - r: 
            return r
        return r | rec(r | newr)
    return rec(r)