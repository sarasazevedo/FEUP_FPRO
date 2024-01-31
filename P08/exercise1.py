'''Consider the recursive solution to the Towers of Hanoi puzzle presented in the notebooks. We want to modify it to output a numbered list of moves. For example, the solution to the puzzle with 3 discs should be output as follows:

1. Move disk from A to C
2. Move disk from A to B
3. Move disk from C to B
4. Move disk from A to C
5. Move disk from B to A
6. Move disk from B to C
7. Move disk from A to C
One way to do this is to extend the recursive definition with an extra parameter representing the current move count: move_tower(height, from_pole, to_pole, with_pole, count) should output the puzzle's solution starting with move number count. The above example is produced by the call move_tower(3, "A", "C", "B", 1).

Define this extended version of the move_tower function.

Hint 1: you may use the fact mentioned in the notebook that the solution to the puzzle with n
 discs takes 2n−1
 moves.

Hint 2: avoid using global variables; this is bad practice and will probably not work with the testing infrastructure used in the quizzes.'''

def move_tower(height, from_pole, to_pole, with_pole, stepN = 1):
    if height > 1:
        stepN = move_tower(height-1, from_pole, with_pole, to_pole, stepN)
        print(f"{stepN}. Move disk from", from_pole, "to", to_pole)
        stepN += 1
        stepN = move_tower(height-1, with_pole, to_pole, from_pole, stepN)
        return stepN
    
    print(f"{stepN}. Move disk from", from_pole, "to", to_pole)
    stepN += 1
    return stepN
