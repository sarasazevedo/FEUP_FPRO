'''Write a Python function cows_bulls(seed_value) that, given an integer seed_value, calls random.seed(seed_value) to initialise the random generator. This function creates a random number with up to 4-digits (correct) and returns a new function that receives one integer parameter. That new function, when called with a number guess, calculates the score of the “bulls and cows” game of the correct versus guess numbers, and returns it as a tuple of the form (cows, bulls). Each guess or correct value is only counted once.

The number of cows is the number of digits guessed in the correct place. The number of bulls is the number of digits guessed correctly but in the wrong place. So, it is a "cows and bulls" version of the game.

For example, if the given seed is 1234, then the generated random number is 7220; if the new function is called with correct=7220 and guess=2240 then the result of that function should be (2, 1).

'''
def cows_bulls(seed_value):
    import random

    random.seed(seed_value)

    def cow(guess):
        num = str(random.randint(0, 9999))
        guess = str(guess)
        guess = list(guess)
        num = list(num)
        cows = 0
        bulls = 0
        check = 0
        while check == 0:
            check = 1
            for i in range(len(num)):
                if num[i] == guess[i]:
                    cows += 1
                    guess.pop(i)
                    num.pop(i)
                    check = 0
                    break
        for i in list(set(guess)):
            if i in num:
                bulls += 1
        return (cows, bulls)

    return cow
