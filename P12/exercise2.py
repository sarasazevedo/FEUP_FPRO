'''Tic-tac-toe, also known as "jogo do galo" in Portugal or "jogo da velha" in Brazil, is a two-player game where each player uses a different symbol, which can be either x or o. The game is played alternately and the goal of each player is to make a line across the board using its symbol.

Write a Python function tic_tac_toe(board, player) that, given a matrix representing the game in the string board, returns where the next move should be played so that the player in the string player wins. Assume there is always one and only one possible winning move for that player.

The board is represented as the string " xx\n o \noxo".

Then, for both player='x' and player='o' the winning move is "A1"
'''

def tic_tac_toe(board, player):
    line = board.split("\n")
    line1 = [x for x in line[0]]
    line2 = [x for x in line[1]]
    line3 = [x for x in line[2]]
    col1 = [x[0] for x in line]
    col2 = [x[1] for x in line]
    col3 = [x[2] for x in line]
    dia1 = [line[0][0], line[1][1], line[2][2]]
    dia2 = [line[0][2], line[1][1], line[2][0]]
    all_lines = [line1, line2, line3, col1, col2, col3, dia1, dia2]
    coords = [(0, 0), (1, 0), (2, 0), (0, 0), (0, 1), (0, 2), (0, 0), (2, 0)]
    letters = ["A", "B", "C"]

    for i in range(len(all_lines)):
        if all_lines[i].count(" ") == 1 and all_lines[i].count(player) == 2:
            coord = all_lines[i].index(" ")
            res = coords[i]
            if i < 3:
                return letters[res[0]] + str(coord + 1)
            elif i < 6:
                return letters[coord] + str(res[1] + coord + 1)
            elif i == 6:
                return letters[coord] + str(coord + 1)
            else:
                if coord == 0:
                    return "A3"
                elif coord == 1:
                    return "B2"
                else:
                    return "C1"
                
