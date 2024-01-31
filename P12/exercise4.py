'''A ball is thrown in a certain cardinal direction. When it hits an obstacle it turns in the angle of the obstacle.

You must return the path of the ball from the beginning until it reaches the goal, represented by the green tile in the figure: (see figure)

The board is defined as a list of strings, such as board = ["E \\", "/ /", " ", "\\ X"], where:

1. ' ' is an empty space
2. '\\' and '/' are corners that change the direction of the ball by 90º
3. 'E', 'N', 'W' and 'S' marks the initial position of the ball and respective cardinal direction of the ball
4. 'X' marks the ending position.

Write a Python function move_ball(board) that, given a board, returns a list with the positions where the ball has travelled through. In the previous example, the return value should be [(0, 0), (0, 1), (0, 2), (1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (3, 1), (3, 2)]

Assume that the ball never leaves the board.
'''
def move_ball(board):
    def pos_inicial(board, lista):
        for j in lista:
            for i in range(len(board)):
                if j in board[i]:
                    return (i, board[i].index(j))

    if "E" in str(board):
        mov = (0, 1)
    elif "W" in str(board):
        mov = (0, -1)
    elif "S" in str(board):
        mov = (1, 0)
    elif "N" in str(board):
        mov = (-1, 0)

    res = []
    new_pos = pos_inicial(board, ["E", "W", "S", "N"])
    res.append(new_pos)

    while True:
        new_pos = (new_pos[0] + mov[0], new_pos[1] + mov[1])
        res.append(new_pos)

        if board[new_pos[0]][new_pos[1]] == "X":
            break
        elif board[new_pos[0]][new_pos[1]] == "\\":
            mov = (mov[1], mov[0])
        elif board[new_pos[0]][new_pos[1]] == "/":
            mov = (-mov[1], -mov[0])

    return res