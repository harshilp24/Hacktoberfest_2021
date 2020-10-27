modules = open("masses.txt" , "r")

def calulate_total_fuel(mass) :
    total_fuel = 0
    fuel = (mass // 3) - 2
    while fuel > 0 :
        total_fuel += fuel
        fuel = (fuel // 3) - 2
    return total_fuel

print(sum([calulate_total_fuel(int(m))  for m in modules]))

