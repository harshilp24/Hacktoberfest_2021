# Implementation of Euclid's algorithm, to find the highest common factor/greates common divisor of two numbers (a,b)
# Author: @incarnadined

def hcf(a, b):
  while a%b: a, b = b, a%b
  return b

a, b = 3, 463
print(hcf(a, b)) # prints 1
