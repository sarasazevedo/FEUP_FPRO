'''Write a function mastermind(guesses, codes) to evaluate a single line of a mastermind game.

The function receives two lists of single character strings. Each string can be "b" for blue, "w" for white and "y" for yellow. The first argument is the user guesses list and the second argument is the codes list containing the correct answer. Each guess corresponds to the correct key in the same position, so the first element of the guesses list corresponds to the first element in the correct list and so forth. Both list arguments have the same length, but can vary in length between tests.

You should return a pair of integers: the first integer is the number of matches in corresponding position and the second integer is the number of matches in an incorrect position.

Note that one right guess (position or color) counts only once.'''
def mastermind(guesses, codes):
    contador = 0
    contador1 = 0
    for g,c in zip (guesses,codes):
        if g == c:
            contador += 1
            
    for g in guesses: 
        if g in codes:
            contador1 += 1
            codes.remove(g)

    return (contador, contador1-contador)