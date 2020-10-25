"""
ROT13 is a simple letter substitution cipher that replaces a letter with the 13th letter 
after it in the alphabet.
"""

def rot13(phrase):
    abc = "abcdefghijklmnopqrstuvwxyz"
    out_phrase = ""
    for char in phrase:
        out_phrase += abc[(abc.find(char)+13)%26]
    return out_phrase

x = "xthexrussiansxarexcoming"
print(rot13(x))


print(rot13(rot13(x)))

#Output :kgurkehffvnafknerkpbzvat

#        xthexrussiansxarexcoming

