"""

Consider the following 4×4 pattern:

 1  2  4  7
 3  5  8 11
 6  9 12 14
10 13 15 16

You are given an integer N. Print the N×N pattern of the same kind (containing integers 1 through N2).

Input

The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and only line of each test case contains a single integer N.

Output

For each test case, print N lines; each of them should contain N space-separated integers.

Constraints

1≤T≤10
1≤N≤100

"""

# cook your dish here
test_cases =  int(input())

def formPattern(size) :
    matrix = [[0 for i in range(size)] for j in range(size)]
    num = 0
    for diag in range(2 * size) :
        for row in range(size) :
            for col in range(size) :
                if row + col == diag :
                    matrix[row][col] = num + 1
                    num += 1
    return matrix
    
for i in range(test_cases) :
    size = int(input()) 
    
    pattern = formPattern(size)
    for i in range(size) :
        for j in range(size) :
            print(pattern[i][j] , end = " ")
        print()
            

