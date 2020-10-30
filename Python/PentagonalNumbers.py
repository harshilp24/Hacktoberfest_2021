"""
Python program to generate series of pentagonal numbers 
These are given by n(3n – 1)/2 with 0, ± 1, ± 2, ± 3…, the first few of which are 
0, 1, 2, 5, 7, 12, 15, 22, 26, 35, …"""

pentagonal_numbers = sum([[i*(3*i - 1)/2, i*(3*i - 1)/2 + i] for i in range(1, 250)], [])

print(pentagonal_numbers)

