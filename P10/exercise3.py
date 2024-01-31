'''A triple (𝑥,𝑦,𝑧) of integers is called Pythagorean if 𝑥2+𝑦2=𝑧2. For example, (3,4,5) is a Pythagorean triple because 32+42=52.

Study the function pythagoreans(n) explored in the lectures that returns a list of Pythagorean triples (𝑥,𝑦,𝑧) such that 𝑥, 𝑦 and 𝑧 are in the range of 1 and n. Write a new version of this function pythagoreans(a, b) that:
1. returns a list of triples where all components are between a and b
2. only returns unique Pythagorean triples, namely the smallest one according to the lexicographical order. For instance, (3,4,5) should be returned but not (4,3,5);
You can use comprehensions but not loops. You cannot use functions sort() or sorted().
'''

def pythagoreans(a:int, b:int):
    return list((x,y,z) for x in range(a,b) for y in range(a,b) for z in range(a,b) if x**2 + y**2 == z**2 and x < y < z)

