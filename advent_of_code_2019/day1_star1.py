f = open("masses.txt" , "r")

def get_weight(mass) :
    return (mass // 3) - 2

print(sum([get_weight(int(i))  for i in f]))

