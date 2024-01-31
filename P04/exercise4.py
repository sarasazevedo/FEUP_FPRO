'''Write a function mastermind(g1, g2, g3, c1, c2, c3) to evaluate a single line of a mastermind game.

The function receives 6 single character strings. Each string can be "b" for blue, "w" for white and "y" for yellow. The first 3 arguments are the user guess. The last 3 arguments are the correct key. Argument g1 is the user guess for the value at argument c1 and so on.

You should give 3 points for each user guess that is completely correct, that is, the same color at the same position in the key and 1 point if the user guessed the color right but at the wrong position (that is, the color exists in the key but at another wrong position).  See the tests for examples.

Note that one right guess (position or color) counts only once.
'''
def mastermind(g1, g2, g3, c1, c2, c3):
    points = 0
    
    if (g1 == c1):
        points += 3
        g1 = "usada"
        c1 = "usada"
        
    if (g2 == c2):
        points += 3
        g2 = "usada"
        c2 = "usada"
        
    if (g3 == c3):
        points += 3
        g3 = "usada"
        c2 = "usada"
        
    if ((g1 == c2) and (c2 != "usada") and (g2 != "usada")):
        points += 1
        c2 = "usada"
        
    elif ((g1 == c3) and (c3 != "usada") and (g3 != "usada")):
        points += 1
        c3 = "usada"
        
    if ((g2 == c1) and (c1 != "usada") and (g1 != "usada")):
        points += 1
        c1 = "usada"
        
    elif ((g2 == c3) and (c3 != "usada") and (g3 != "usada")):
        points += 1
        c3 = "usada"
        
    if ((g3 == c1) and (c1 != "usada") and (g1 != "usada")):
        points += 1
        c1 = "usada"
        
    elif ((g3 == c2) and (c2 != "usada") and (g2 != "usada")):
        points += 1
        c2 = "usada"
        
    return points
