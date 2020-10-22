""" *Amicable numbers* are two different numbers so related that the sum of the proper divisors of each is equal to the other number.
A proper divisor of a number is a positive factor of that number other than the number itself.
For example, the proper divisors of 6 are 1, 2, and 3.
"""
#finding proper divisors of a number and returning its  sum
def divisors(n):
  return sum(list(i for i in range(1,n) if n % i == 0))
#this function checks if any numbers have equal sum of the proper divisors 
def Amicable_numbers(LIMIT):
  return list((i,j) for i in range(LIMIT) for j in range(LIMIT) if divisors(i) == j and divisors(j) == i and i > j)

print(Amicable_numbers(500))
 
# In the range 500 there is only one amicable pair .

# Output: 
# [(284, 220)]


