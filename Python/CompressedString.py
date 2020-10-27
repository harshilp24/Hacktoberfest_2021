"""
The string should be compressed such that consecutive duplicates
of characters are replaced with the character and followed by 
the number of consecutive duplicates"""

from itertools import groupby

def CompressedString(string):
    values = []
    compressed_string = ""
    for key, value in groupby(string):
        values.append(list(value))
    for i in values:
        if(len(i) >= 3):
            compressed_string += i[0] + str(len(i))
        else:
            compressed_string += "".join(i)
    return compressed_string

print(CompressedString("aaaabbbccddddde"))

#Output : a4b3ccd5e

