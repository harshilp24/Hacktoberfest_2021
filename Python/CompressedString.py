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
