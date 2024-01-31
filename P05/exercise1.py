'''Write a Python function rm_letter_rev(ch, s) that removes all occurrences of a given character ch (case sensitive) from the given string s (case sensitive) and returns the resulting string with its characters in the reverse order.'''

def rm_letter_rev(ch,s):
    srev=""
    for c in s:
        if(c!=ch):
            srev = c + srev
    return srev 
