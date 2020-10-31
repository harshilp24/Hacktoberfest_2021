#Alexandrian integers : numbers of the form n=pqr such that 1/n = 1/p + 1/q + 1/r for some integers p,q,r. For example, 630 is an Alexandrian integer(p=5, q=-7,r=-18)
#Reference  Link : (Project Euler, Problem 221) https://projecteuler.net/problem=221#:~:text=For%20example%2C%20630%20is%20an,the%20150000th%20Alexandrian%20integer.

def is_alexandrian():
    a = [i*j*k for i in range(-100,0) for j in range(i + 1,0) for k in range(0,1000) if i*j + j*k + k*i == 1]
    a.sort()
    return a 

print(is_alexandrian())

