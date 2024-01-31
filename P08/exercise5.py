'''Write a function soup(matrix, word) that, given a matrix of letters, returns the first location of the word in the matrix, or None if not found.

For example, let's say we have the following matrix and are trying to find the word "PORTO".
Then the function returns "E2" because the word starts in line=E, column=2.

Notice that the words can use any cardinal direction: north, east, south, west.

All letters are given in upper-case and the function returns the first occurrence of the word using lexicographical order (i.e. if the word can be found in "A4" and "B2", then it returns "A4"). You may want to use chr() and ord() to have the line as a letter.

Hint: write an auxiliary recursive function soup_rec(matrix, word, line, col) that attempts to find a word at a given line and column. The function soup should just call this auxiliary function with suitable arguments.'''
def soup(matrix, word):
    def soup_rec(matrix, word, line, col):
        if word == "":
            return True
        
        if matrix[line][col] != word[0]:
            return False
        
        for l in [line-1,line,line+1]:
            for c in [col-1,col,col+1]:
                if l != line and c != col:
                    continue
                if l == line and c == col:
                    continue
                try:
                    if soup_rec(matrix, word[1:], l, c): return True
                except: pass
        return False
    
    for l in range(len(matrix)):
        for c in range(len(matrix[0])):
            if soup_rec(matrix, word, l, c): return f"{chr(ord('A')+l)}{c+1}"
                