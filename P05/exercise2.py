'''Write a Python function camel_case(phrase) to convert a given string phrase to the camelCase format.
Camel case (sometimes stylized as camelCase or CamelCase, also known as camel caps or more formally as medial capitals) is the practice of writing phrases without spaces or punctuation, indicating the separation of words with a single "uppercase" (capital) letter, and the first letter always "lowercase" (minuscule).'''
import string

def camel_case(pharase):
    result = ""
    upper = False
    for ch in pharase: 
        if(ch.isalpha()):
            if upper:
                result += ch.upper()
                upper = False
            else:
                result += ch.lower()
        else:
            upper=True
    return result
